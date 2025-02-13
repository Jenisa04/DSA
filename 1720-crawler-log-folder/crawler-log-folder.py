class Solution:
    # Jenisa
    def minOperations(self, logs: List[str]) -> int:
        record = [] #record stack
        for i in logs: 
            if i == '../':
                if record:
                    record.pop()
            elif i != './':
                record.append(i)
        
        return len(record)
