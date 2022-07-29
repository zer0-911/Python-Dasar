total_teman = int(input())
total_bill = int(input())

fix_pajak = total_bill*(20/100)
fix_bill = total_bill+fix_pajak
fix_bayar = fix_bill/total_teman

print(fix_bayar)
