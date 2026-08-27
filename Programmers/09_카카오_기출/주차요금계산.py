def solution(fees, records):
    # 길이가 딱 맞으면 자동 언패킹 가능 
    basic_time, basic_fee, unit_time, unit_fee = fees
    answer = [] # 차량 번호가 작은 자동차부터 주차 요금 차례로 return
    in_dict = {} # {차량번호:입차시각}
    total_time = {} # {차량번호:총 누적 분}
    for record in records:
        time, car, state = record.split() 
        # 2. in이면 (차량번호, 입차시각)
        if state == 'IN':
            in_dict[car] = time
        # 3. out이 나오면 누적 시간에 넣기
        elif state == "OUT":
            in_time = in_dict[car]
            # 분 단위로 계산 (시간 * 60 + 분)
            in_min = int(in_time[:2]) * 60 + int(in_time[3:])
            out_min = int(time[:2]) * 60 + int(time[3:])
            
            # 누적 시간 딕셔너리에 시간 더해주기
            if car in total_time:
                total_time[car] += (out_min - in_min)
            else:
                total_time[car] = (out_min - in_min)
                
            del in_dict[car] # 정산 끝났으니 주차장에서 차 빼기

    # 4. 23:59까지 안 나간 차들 강제 출차 및 시간 누적
    last_min = 23 * 60 + 59
    for car, in_time in in_dict.items():
        in_min = int(in_time[:2]) * 60 + int(in_time[3:])
        if car in total_time:
            total_time[car] += (last_min - in_min)
        else:
            total_time[car] = (last_min - in_min)
    # 5. 누적된 시간을 바탕으로 '요금'을 딱 한 번씩만 계산!
    answer = []
    # 차량 번호가 작은 순서대로 정렬해야 하니까 딕셔너리 키값을 정렬해서 돌리기
    for car in sorted(total_time.keys()): 
        time_spent = total_time[car]
        
        if time_spent <= basic_time:
            fee = basic_fee
        else:
            fee = basic_fee + -((basic_time - time_spent) // unit_time) * unit_fee
            
        answer.append(fee)
        
    return answer
