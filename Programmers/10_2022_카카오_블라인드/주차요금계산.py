def solution(fees, records):
    answer = [] # 차량 번호가 작은 자동차부터 주차 요금 차례로 return
    in_list = set()
    result_dict = {}
    # 1. [0:5] 시각 , [6:10] 차량번호 [11:13] 인 [11:14] 아웃
    for record in records:
        fee = 0
        # 2. in이면 (차량번호, 입차시각)
        if len(record) == 13:
            in_list.add((record[6:10], record[0:5]))
        # 3. out이 나오면 in 리스트에서 차량번호 찾아서 -> 요금 계산
        elif len(record) == 14:
            if record[6:10] in in_list:
                car = record[6:10]
                in_min = int(in_list[car][0:2])*60 + int(in_list[car][3:5])
                out_min = int(record[0:2])*60+int(record[3:5])
                total = out_min - in_min
                if total <= fees[0]:
                    fee = fees[1]
                else:
                    total = fees[0] - total
                    fee = -(total//fees[2]) * fees[3]
            # 4. {'차랑번호':'청구요금'} if 차량번호 존재-> 청구요금에 ++
            if record[6:10] in result_dict:
                result_dict[record[6:10]] += fee
            else:
                result_dict[record[6:10]] = fee
    # 5. in_list에 남아 있는 차량 번호와 시각 -> 전부 23:59로 처리
    last = 23*60+59
    for car in in_list:
        fee = 0
        # 요금 계산부터
        in_min = int(car[1][0:2])*60+int(car[1][3:5])
        total = last-in_min
        if total <= fees[0]:
            fee = fees[1]
        else:
            total = fees[0] - total
            fee = -(total//fees[2]) * fees[3]
            
        if car[0] in result_dict:
            result_dict[car[0]] += fee
        else:
            result_dict[car[0]] = fee
    print(result_dict)
    for key, values in result_dict:
        answer.append(key)
    answer.sort()
    return answer
