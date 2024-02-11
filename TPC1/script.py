def find_interval(x, interval_size=5, start=0):
    interval_start = start + (x // interval_size * interval_size)
    return (interval_start, interval_start + interval_size - 1)


if __name__ == "__main__":
    file =  open("emd.csv")
    data = file.read()
    lista = []

    for line in data.split("\n")[1:]:
        camps = line.split(",")
        if len(camps) == 13:
            lista.append({
                    "id": camps[0],
                    "index": camps[1],
                    "dataEMD": camps[2],
                    "primeiro": camps[3],
                    "ultimo": camps[4],
                    "idade": camps[5],
                    "genero": camps[6],
                    "morada": camps[7],
                    "modalidade": camps[8],
                    "clube": camps[9],
                    "email": camps[10],
                    "federado": camps[11],
                    "resultado": camps[12]
                    })

    lista.sort(key=lambda x: x["modalidade"])

    for atleta in lista:
        print(atleta)

    aptos = len(list(filter(lambda x: x["resultado"] == "true", lista)))

    rate_aptos = aptos / len(lista) * 100

    print("Percentagem de atletas aptos: " + str(round(rate_aptos,2)) + "%\nPercentage de atletas não aptos: " + str(round(100 - rate_aptos,2)) + "%")


    intervals = {}
    for atleta in lista:
        interval = find_interval(int(atleta["idade"]))
        if interval in intervals:
            intervals[interval] += 1
        else:
            intervals[interval] = 1

    for interval in intervals:
        print("[" + str(interval[0]) + "-" + str(interval[1]) + "]: " + str(intervals[interval]))