class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = encoded + string + "嗨"
        return encoded

    def decode(self, s: str) -> List[str]:
        if s:
            return s.split("嗨")[:-1]
        return []
