#include<memory>

using namespace std;

class Board{
    int size;
    public:
        Board(){}
        void click(int x,int y);
};

enum class BlockType{EMPTY,VALUE,BOMB};

class Block{
    BlockType type = BlockType::EMPTY;
    bool visible = false;

    public:
        Block(BlockType type):type(type){}
        void setVisible(){visible=true;}
};

class ValueBlock:public Block{
    int val;
    public:
        ValueBlock(BlockType type,int val):Block(type),val(val){}
        int getValue(){return val;}
};

class Display{
    private:
        shared_ptr<Board> board;

    public:
        Display(shared_ptr<Board> board):board(board){}
        void printBorad(){}
};

class Player{


    public:
        Player(){}
        void click(int x,int y);
};

class Game{
    private:
        shared_ptr<Player> player;
        shared_ptr<Board> board;
        shared_ptr<Display> display;
        int size;

    public:
        Game(int size):size(size){
            player = make_shared<Player>();
            board = make_shared<Board>();
            display = make_shared<Display>(board);

        }
        shared_ptr<Player> getPlayer(){return player;}
        shared_ptr<Board> getBoard(){return board;}
        shared_ptr<Board> getDisplay(){return board;}
};
