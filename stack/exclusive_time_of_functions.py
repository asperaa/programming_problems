"""Exclusive time of functions"""
def exclusive_time(n, logs):
        stack = []
        result = [0] * n
        prev_time = 0
        for log in logs:
            f_id, typ, time = log.split(":")
            f_id, time = int(f_id), int(time)
            if typ == "start":
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(f_id)
                prev_time = time
            else:
                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return result  


if __name__ == "__main__":
    n = 2
    # logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
    logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
    print(exclusive_time(n, logs))