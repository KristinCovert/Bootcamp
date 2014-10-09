/**
 * Created by student on 10/6/14.
 */
//This way we are appending the list of costs from the receipt by what the person says they
//have eaten.

function(){
    var table_receipt ={}
    var item_name = prompt ("Enter the first item on the receipt: ")
    var item_cost = prompt ("How much was the item?")
    table_receipt["item_name"] = item_cost
    console.log(table_receipt)
    //for loop to continue adding objects
}
//
//
//var receipt = {"chicken": 8.0, "salad":6.9, "soda":1.1};
//var name = ["c", "s", "a"];
//var nameCosts = [];
//name.total = 0;
//
//for (var thing in receipt) {
//    nameCosts.push(receipt[thing]);
//    console.log(nameCosts)
//}
//
////Here is a way to add up all that the person had
//var nameCosts = 0
//
//for(var thing in receipt){
//  nameCosts += (receipt[thing]);
//}
//
////Define the variables and calculate the tip multiplier//
//var people = prompt("How many people are in your party? ");
//var bill = prompt("How much was your bill? ");
//var tip = prompt("How much would you like tip? 15, 20, or 25 %? ")
//tip = tip / 100;
////if else to change tip multiplier based on party size. More than 6 people requires a greater tip.//
//if (people < 6) {
//alert("Your total tip is $" + bill * tip + ". Press return for your individual total. ");
//new_bill = (bill * (1 + tip)) / people;
//new_bill = new_bill.toFixed(2);
//alert("Your individual bill is $" + new_bill);
//}
////Because tip must be at least 18% the 15% choice doesn't apply and user must choose a higher one.//
//else {
//if(tip === .15) {
//alert("Hey cheapskate, the minimum is 18%! Press return to choose a more suitable amount. ")
//var larger_tip = prompt("Would you like to do 18, 20 or 25%? ")
//larger_tip = larger_tip / 100
//alert("Your total tip is $" + bill * larger_tip + ". Press return for your individual total. ");
//new_bill = (bill * (1 + larger_tip)) / people;
//new_bill = new_bill.toFixed(2);
//alert("Your individual bill is $" + new_bill);
//}
//else {
//alert("<hey big tipper, your gratuity is $" + bill * tip + ". Press return for your individual total. ");
//new_bill = (bill * (1 + tip)) / people;
//new_bill = new_bill.toFixed(2);
//alert("Your individual bill is $" + new_bill);
//}
