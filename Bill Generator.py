import pandas as pd

carts = []

def add_items():
    print("\nAdd New Items in Cart...")
    input_name = input("\nEnter the Item Name...").strip().title()
    
    try:
        price = float(input("\nEnter the price of Item:"))
        quantity = int(input("\nEnter The Quantity:"))
        
        item_total_price = price*quantity
        
        items = {
            'Item' : input_name,
            'Price' : price,
            'Quantity' : quantity,
            'Total' : item_total_price
            }
        
        carts.append(items)
        print(f"\nItems Added Successfully({quantity} x {input_name})")
        
        print("\nCurrent Cart Detail...")
        df = pd.DataFrame(carts)
        df.index = range(1,len(df) + 1)
        
        print('\n',df)
        
    except ValueError:
        print("\nInvalid Input : Please Give number in Price & Quantity!")
        
def final():
    if not carts:
        print('\nCart is Empty!,Add Items to Cart...!')
        return
        
    df_bill =pd.DataFrame(carts)
    df_bill.index = range(1,len(df_bill) + 1)
    
    sub_total = df_bill['Total'].sum()
    gst = sub_total * 0.05
    
    final_total = sub_total + gst
    
    print('\n' + '='*50)
    print(f"{'Python Supermarket':^50}")
    print('='*50)
    
    print("\n Purchase Items.......")
    print(df_bill.to_string())
    
    summary ={
        'Bill Types' : ['Sub Total','GST(5%)','Final Total'],
        'Amount' : [f"Rs.{sub_total:.2f}",f"Rs.{gst:.2f}",f"Rs.{final_total:.2f}"]
    }
    
    summary_df = pd.DataFrame(summary)
    print("\n   Final Bill Summary")
    print("-"*30)
    print(summary_df.to_string(index= False))
    print("-"*30)
    
    print(f"\n{'Thanks For Visiting':^50}")
        
def menu():
    print("\n>>>>>>>>>>>>> Mini Bill Generator <<<<<<<<<<<<")
    print("\n1.Add Item in Cart....")
    print("2.Final Bill and Exit....")

def main():
    while True:
        menu()
        choose = input("\nEnter Your Choice Number:").strip()
        
        if choose == "1":
            add_items()
        
        elif choose == "2":
            final()
            break
        
        else:
            print("\nPlease Choose Between(1 and 2)")
        
if __name__ == '__main__':
    main()