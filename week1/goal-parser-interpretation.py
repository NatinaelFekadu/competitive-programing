class Solution:
    def interpret(self, command: str) -> str:
        hashmap = {
            "G":"G",
            "()":"o",
            "(al)":"al"
        }
        parsed = ""
        for i in range(len(command)):
            if command[i] == ")":
                if command[i-1] == "(":
                    parsed += hashmap["()"]
                else:
                    parsed += hashmap["(al)"]
            elif command[i] == "G":
                parsed += hashmap["G"]

            else:
                continue
        return parsed