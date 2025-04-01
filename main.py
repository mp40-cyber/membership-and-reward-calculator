from tabulate import tabulate
import random


class MembershipUser():

    data = {"Lana" : "Platinum",
        "Caya" : "Gold",
        "Mega" : "Gold",
        "Ojan" : "Silver",
        "John" : "Platinum",
        }
    
    
    def __init__(self, username, expense, income):
        self.username = username
        self.expense = expense / 1_000_000
        self.income = income / 1_000_000
        self.predicted_membership = None

    def benefit_membership(self):
        table = [["Discount 15%", "Discount 10%", "Discount 8%"],
                 ["Benefit Silver", "Benefit Silver", "Voucher Makanan"],
                 ["Gold", "Voucher Ojek Online",""],
                 ["Voucher Liburan", "", ""],
                 ["Cashback max. 30%", "", ""],
                 ]
        headers = ["Tier Platinum", "Tier Gold", "Tier Silver"]
        print("PacECommerce Benefit List")
        print("")
        print(tabulate(table, headers=headers, tablefmt="grid"))

    def tier_requirements(self):
        table = [["Tier Platinum", "8 Mil/Month", "17 Mil/Month"],
                 ["Tier Gold", "6 Mil/Month", "10 Mil/Month"],
                 ["Tier Silver", "5 Mil/Month","7 Mil/Month"],
                ]
        headers = ["Tier", "Min Expense", "Min Income"]
        print("Requirement To Achieve Or Upgrade Tier")
        print("")
        print(tabulate(table, headers=headers, tablefmt="grid"))

    def user_prediction(self):
        tiers = {
            "Platinum": (8, 15),
            "Gold": (6, 10),
            "Silver": (5, 7),
        }
        jarak_tier = {}
        for tier, (tier_expense, tier_income) in tiers.items():
            distance = ((tier_expense - self.expense) ** 2 + (tier_income - self.income) ** 2) ** 0.5
            jarak_tier[tier] = round(distance, 2)

        self.predicted_membership = min(jarak_tier, key=jarak_tier.get)  # Simpan hasil prediksi
        print(f"\nPrediksi Membership: {self.predicted_membership}")

        # Tambahkan ke dictionary hanya jika user belum ada
        if self.username not in self.data:
            self.data[self.username] = self.predicted_membership
            print(f"User baru ditambahkan: {self.username} → {self.predicted_membership}")
        else:
            print(f"{self.username} sudah ada dalam data dengan membership {self.data[self.username]}")

     
    def calculate_price(self, total_belanja):
        if self.predicted_membership is None:
            print("Error: Prediksi membership belum dilakukan!")
            return
        membership = self.predicted_membership
        membership = membership.lower()
        if membership == "platinum":
            list_prize = ["Voucher Makanan", "Gold 0.5 gr", "Voucher Liburan", "Cashback max. 30%",
                          "None", "None", "None"]
            prize = random.choice(list_prize)
            if prize == "Cashback max. 30%":
                cashback_list = [0.05, 0.5, 0.05, 0.10, 0.10, 0.15, 0.15, 0.20, 0.25, 0.30]
                cashback = random.choice(cashback_list)
                nilai_cashback = cashback * total_belanja
                print (f'Selamat! Anda Mendapatkan Cashback Sebesar : {nilai_cashback}')
            diskon = 0.15 * total_belanja
            harga_setelah_potongan = total_belanja - diskon
            print (f'Anda Mendapat Diskon Sebesar : {diskon}')
            print (f'Total Yang Harus Dibayar Adalah : {harga_setelah_potongan}')
            print (f'Hadiah yang didapat : {prize}')
        elif membership == "gold":
            list_prize = ["Voucher Makanan", "Voucher Ojek Online", "None", "None",]
            prize = random.choice(list_prize)
            diskon = 0.10 * total_belanja
            harga_setelah_potongan = total_belanja - diskon
            print (f'Anda Mendapat Diskon Sebesar : {diskon}')
            print (f'Total Yang Harus Dibayar Adalah : {harga_setelah_potongan}')
            print (f'Hadiah yang didapat : {prize}')
        elif membership == "silver":
            list_prize = ["Voucher Makanan", "None",]
            prize = random.choice(list_prize)
            diskon = 0.08 * total_belanja
            harga_setelah_potongan = total_belanja - diskon
            print (f'Anda Mendapat Diskon Sebesar : {diskon}')
            print (f'Total Yang Harus Dibayar Adalah : {harga_setelah_potongan}')
            print (f'Hadiah yang didapat : {prize}')
        else :
            print ('Jenis Membersip tidak valid')


# user1 = MembershipUser("HeraMaulana", 7000000, 9000000)
# user1.user_prediction()
# user1.calculate_price(750000)

user2 = MembershipUser("Renzo", 8000000, 124000000)
# user2.user_prediction()
# user2.calculate_price(800000)
user2.calculate_price(765000)
