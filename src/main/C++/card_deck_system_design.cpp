#include<iostream>
#include<string>
#include<vector>

enum class SuiteType{
    SPADE,
    CLUBS,
    DIAMOND,
    HEARTS
};

enum class Status
{
    IN,
    OUT
};

class Suite
{
    SuiteType suiteType;
    std::string suiteName;

public:
    Suite(SuiteType suiteType, std::string suiteName):suiteType(suiteType),suiteName(suiteName){}
    std::string getSuiteName(){ return suiteName; }
    SuiteType getSuiteType(){ return suiteType;}
};

class Card
{
private:
    std::string value;
    Suite suite;
    Status status = Status::IN;

public:
    Card(std::string value, Suite suite):value(value),suite(suite){}
    Suite getSuite(){ return suite; }
    std::string getValue(){ return value; }
    void printCard(){ std::cout<<"Suite:" << suite.getSuiteName() <<" Value:"<< value << std::endl; }

};

class CardDeck
{
private:
    const int SIZE=52;
    int inCount=52;
    
    std::vector<Card> cards;
    const std::vector<std::string> VALUES{"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
    const std::vector<Suite> SUITES{Suite(SuiteType::DIAMOND,"DIAMOND"),
                                    Suite(SuiteType::SPADE,"SPADE"),
                                    Suite(SuiteType::CLUBS,"CLUBS"),
                                    Suite(SuiteType::HEARTS,"HEARTS")};

protected:
public:
    CardDeck(){
        for(auto& s:SUITES){
            for(auto& v:VALUES){
                cards.push_back(Card(v,s));
            }
        }
    }

    int getAvailableCount(){ return inCount; }

    void printCards(){
        for(auto& card:cards){
            card.printCard();
        }
    }
};


int main(){
    CardDeck deck;
    deck.printCards();
    return 0;
}