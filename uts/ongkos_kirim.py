delivery_type = input("Jenis pengiriman (Ekspres/Reguler): ")
package_weight = float(input("Berat paket (dalam kg): "))

def outputs(type, weigt, price):
    return f"\nJenis pengiriman : {type}" + f"\nBerat paket : {weigt} Kg" + f"\nTarif pengiriman : Rp. {price}"

def result(delivery_type, package_weight):
    if (delivery_type.lower() == "ekspres"):
        if (package_weight < 1):
            return outputs(delivery_type, package_weight, 50000)
        elif (1 <= package_weight <= 5):
            return outputs(delivery_type, package_weight, 100000)
        else: 
            return outputs(delivery_type, package_weight, 200000)
    elif (delivery_type.lower() == "reguler"):
        if (package_weight < 1):
            return outputs(delivery_type, package_weight, 20000)
        elif (1 <= package_weight <= 5):
            return outputs(delivery_type, package_weight, 50000)
        else: 
            return outputs(delivery_type, package_weight, 100000)
    else:
        return "Pengiriman tidak valid"
    

print(result(delivery_type, package_weight))


