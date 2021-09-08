#include<iostream>
#include <queue> 

using namespace std;

using Price = unsigned;
using Volume = unsigned;
using UserReference = int;
using OrderId = int;
using OrderId = int;

enum class Side { Buy, Sell };

class Order{
	string symbol;
	Side side;
	Price price;
	Volume volume;
	UserReference userReference;
    int seqNo = 0; 

    public:
        Order(string symbol, Side side, Price price, Volume volume, UserReference userReference)
        :symbol(symbol),side(side),price(price),volume(volume),userReference(userReference){};
        
        Side getSide(){return side;}
        Price getPrice(){return price;}
        int getSeqNo(){return seqNo;}
        Volume getVolume(){return volume;}
        UserReference getUserReference(){return userReference;}

        void setSeqNo(int seq_no){seqNo = seq_no;}
        
        void print(){
            cout<<price<<"\t"<<volume<<"\t"<<userReference<<endl;
        }

};

class CompareSellOrders
{
    public:
        bool operator() (Order a, Order b)
        {
            if (a.getPrice() > b.getPrice())
                return true;
            else if(a.getPrice() == b.getPrice()){
                if (a.getSeqNo() > b.getSeqNo())
                    return true;
            }
            
            return false;
        }
};

class CompareBuyOrders
{
    public:
        bool operator() (Order a, Order b)
        {
            if (a.getPrice() < b.getPrice())
                return true;
            else if(a.getPrice() == b.getPrice()){
                if (a.getSeqNo() > b.getSeqNo())
                    return true;
            }
            
            return false;
        }
};


class OrderBook
{
	private:
		priority_queue<Order,vector<Order>, CompareBuyOrders> buySide;
        priority_queue<Order,vector<Order>, CompareSellOrders> sellSide;
        int nextSeqNo = 0;
	public:
        OrderBook(){};
		void addOrder(Order order);
        void print();
};

void OrderBook::addOrder(Order order){
    order.setSeqNo(++nextSeqNo);
    if (order.getSide() == Side::Buy){
        buySide.push(order);
    }
    else if (order.getSide() == Side::Sell){
        sellSide.push(order);
    }
    else{
        //error
    }

}

void OrderBook::print()
{
    cout<<"Printing Sell Orders"<<endl;
    auto temp = sellSide;
    while(!temp.empty()){
        auto ord = temp.top();
        ord.print();
        temp.pop();
    }
    cout<<endl;

    cout<<"Printing Buy Orders"<<endl;
    auto temp2 = buySide;
    while(!temp2.empty()){
        auto ord = temp2.top();
        ord.print();
        temp2.pop();
    }
}

int main(){
    cout<<"starting execution"<<endl;
    OrderBook order_book;

    order_book.addOrder(Order("ABC",Side::Buy, 20, 500, 200001));
    order_book.addOrder(Order("ABC",Side::Buy, 25, 600, 200002));
    order_book.addOrder(Order("ABC",Side::Buy, 25, 700, 200003));
    order_book.addOrder(Order("ABC",Side::Sell,20, 500, 100001));
    order_book.addOrder(Order("ABC",Side::Sell, 25, 600, 100002));
    order_book.addOrder(Order("ABC",Side::Sell, 25, 700, 100003));

    order_book.print();

    return 0;
}