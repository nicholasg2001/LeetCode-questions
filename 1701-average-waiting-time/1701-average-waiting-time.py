class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        total_waiting_time = 0
        current_time = 0


        for arrival, time in customers:
            if current_time < arrival:
                current_time = arrival
            waiting_time = current_time - arrival + time
            total_waiting_time += waiting_time
            current_time += time
        
        return total_waiting_time / len(customers)
