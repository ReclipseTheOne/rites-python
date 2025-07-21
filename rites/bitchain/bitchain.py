class BitChain:
    """
    Wrapper for bit chain manipulation (bit-level logic).
    Supports bitwise operations, conversions, and masking with offsets.
    """

    def __init__(self, value=0, bit_length=None):
        if isinstance(value, bytes):
            self.value = int.from_bytes(value, 'big')
        elif isinstance(value, str) and set(value) <= {'0', '1'}:
            self.value = int(value, 2)
        else:
            self.value = int(value)
        self._bit_length = bit_length or self.value.bit_length()

    def __and__(self, other): return BitChain(self.value & int(other), self._bit_length)
    def __or__(self, other): return BitChain(self.value | int(other), self._bit_length)
    def __xor__(self, other): return BitChain(self.value ^ int(other), self._bit_length)
    def __invert__(self): return BitChain(~self.value & ((1 << self._bit_length) - 1), self._bit_length)
    def __lshift__(self, n): return BitChain(self.value << n, self._bit_length + n)
    def __rshift__(self, n): return BitChain(self.value >> n, max(1, self._bit_length - n))

    def __int__(self): return self.value
    def __len__(self): return self._bit_length
    def __str__(self): return self.to_bin()
    def __repr__(self): return f"BitChain({self.to_bin()})"

    def to_bin(self) -> str:
        return bin(self.value)[2:].zfill(self._bit_length)

    def to_bytes(self) -> bytes:
        byte_len = (self._bit_length + 7) // 8
        return self.value.to_bytes(byte_len, 'big')

    def to_hex(self) -> str:
        return hex(self.value)

    def slice(self, start: int, end: int) -> "BitChain":
        """Extrage biții [start:end) din lanț."""
        if end <= start:
            raise ValueError("End must be greater than start.")
        mask = (1 << (end - start)) - 1
        return BitChain((self.value >> start) & mask, end - start)

    def mask(
        self,
        other: "BitChain",
        left_offset: int = 0,
        right_offset: int = 0,
        op: str = "AND"
    ) -> "BitChain":
        """
        Apply a BitChain as a mask, with offsets and a logical operation.
        If the offset makes it such that the mask doesn't overlap fully,
        the operation will still apply, but only to the overlapping bits.

        Applicable ops: AND, OR, XOR, NAND, NOR, XNOR, REPLACE
        """
        ops = {
            "AND": lambda a, b: a & b,
            "OR": lambda a, b: a | b,
            "XOR": lambda a, b: a ^ b,
            "NAND": lambda a, b: ~(a & b),
            "NOR": lambda a, b: ~(a | b),
            "XNOR": lambda a, b: ~(a ^ b),
            "REPLACE": lambda a, b: b
        }

        op = op.upper()
        if op not in ops:
            raise ValueError(f"Unsupported bit operation: {op}")

        total_offset = left_offset - right_offset
        mask_len = len(other)
        base_len = self._bit_length

        # Determine overlap
        if total_offset >= 0:
            mask_start = total_offset
            mask_end = min(mask_start + mask_len, base_len)
            overlap_len = max(0, mask_end - mask_start)
        else:
            mask_start = 0
            mask_end = min(mask_len, base_len + total_offset)
            overlap_len = max(0, mask_end - mask_start)

        if overlap_len == 0:
            # No overlap, just return self unchanged
            return BitChain(self.value, self._bit_length)

        # Prepare mask for overlap
        if total_offset >= 0:
            mask_bits = (int(other) >> (mask_len - overlap_len)) & ((1 << overlap_len) - 1)
            mask_val = mask_bits << mask_start
        else:
            mask_bits = (int(other) >> (mask_len - overlap_len - (-total_offset))) & ((1 << overlap_len) - 1)
            mask_val = mask_bits << 0

        # Prepare base for operation
        base_mask = ((1 << overlap_len) - 1) << (mask_start if total_offset >= 0 else 0)
        base_val = self.value

        # Apply operation only on overlapping bits
        base_overlap = (base_val & base_mask)
        mask_overlap = (mask_val & base_mask)
        result_overlap = ops[op](base_overlap, mask_overlap) & base_mask
        result = (base_val & ~base_mask) | result_overlap

        return BitChain(result, self._bit_length)

    @staticmethod
    def apply_mask(
        base: "BitChain",
        mask: "BitChain",
        left_offset: int = 0,
        right_offset: int = 0,
        op: str = "AND"
    ) -> "BitChain":
        """
        Apply a BitChain as a mask over another BitChain, with offsets and a logical operation.
        If the offset makes it such that the mask doesn't overlap fully,
        the operation will still apply, but only to the overlapping bits.

        Applicable ops: AND, OR, XOR, NAND, NOR, XNOR, REPLACE
        """
        return base.mask(mask, left_offset, right_offset, op)
