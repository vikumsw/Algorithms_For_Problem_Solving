#include<memory>
#include<iostream>
#include<unordered_map>

using namespace std;

enum class Sides{TOP,BOTTOM,LEFT,RIGHT};
enum class Colour{WHITE,BLACK};

class Piece{
    Colour colour;

    public:
        Piece(Colour colour):colour(colour){}
        void flip(){
            if (colour==Colour::WHITE)
                colour = Colour::BLACK;

            colour = Colour::WHITE;
        };
        bool isCaptured();
        Colour getColour(){return colour;}

};

class Board{
    using p_Piece = unique_ptr<Piece>;
    using Score = int;

    private:
        p_Piece mat[10][10];
        unordered_map<Colour,Score> scores;
    public:
        Board(){
            cout<<"Constructing board"<<endl;
            scores.insert({Colour::BLACK,0});
            scores.insert({Colour::WHITE,0});
        }
        void addPiece(int x,int y, Colour colour){
            mat[x][y]= move(make_unique<Piece>(colour));
            scores[colour]++;

            Colour opp_colour = getOpposite(colour);
            
            if (y-2>=0 && mat[x][y-2]!=nullptr && mat[x][y-2]->getColour() == colour && mat[x][y-1]!=nullptr && mat[x][y-1]->getColour() == opp_colour){
                mat[x][y-1]->flip();
                scores[colour]++;
                scores[opp_colour]--;
            }
            if (y+2>=0 && mat[x][y+2]!=nullptr && mat[x][y+2]->getColour() == colour && mat[x][y+1]!=nullptr && mat[x][y+1]->getColour() == opp_colour){
                mat[x][y+1]->flip();
                scores[colour]++;
                scores[opp_colour]--;
            }
            if (x-2>=0 && mat[x-2][y]!=nullptr && mat[x-2][y]->getColour() == colour && mat[x-1][y]!=nullptr && mat[x-1][y]->getColour() == opp_colour){
                mat[x-1][y]->flip();
                scores[colour]++;
                scores[opp_colour]--;
            }
            if (x+2>=0 && mat[x+2][y]!=nullptr && mat[x+2][y]->getColour() == colour && mat[x+1][y]!=nullptr && mat[x+1][y]->getColour() == opp_colour){
                mat[x+1][y]->flip();
                scores[colour]++;
                scores[opp_colour]--;
            }

        }
        int getScore(Colour colour){
            return scores[colour];
        }
        void printScores(){
            cout<<"White:"<<getScore(Colour::WHITE)<<endl;
            cout<<"Black:"<<getScore(Colour::BLACK)<<endl;
        }
        Colour getOpposite(Colour colour){
            if (colour==Colour::WHITE)
                return Colour::BLACK;

            return Colour::WHITE;
        }
};

class Player;

class Othello
{
    using p_Othello=shared_ptr<Othello>;
    using p_Player=shared_ptr<Player>;
    using p_Board=shared_ptr<Board>;
    

    private:
        unordered_map<Colour,p_Player> players;
        int maxTimePerMove = 120;
        p_Board board;
        static Othello* game;
        

        Othello()
        {
            players[Colour::WHITE] = make_shared<Player>(Colour::WHITE);
            players[Colour::BLACK] = make_shared<Player>(Colour::BLACK);
            board = make_shared<Board>();
        }

        

    public:
        
        static Othello* getGame()
        {
            if (game == nullptr)
            {
                game  = new Othello;
            }

            return game;
            
        }
        p_Player getPlayer(Colour c){
            return players[c];
        }
        p_Board getBoard(){
            return board;
        }
};

class  Player{
    private:
        Colour colour;
    
    public:
        Player(Colour colour):colour(colour){}
        Colour getColour();

        // creates a piece at pos x,y
        void playTurn(int x,int y){
            Othello::getGame()->getBoard()->addPiece(x,y,colour);
        }
};

Othello* Othello::game=nullptr;

int main(){
    cout<<"Starting Game"<<endl;

    Othello* game = Othello::getGame() ;
    auto pW = game->getPlayer(Colour::WHITE);
    auto pB = game->getPlayer(Colour::BLACK);

    pW->playTurn(5,5);
    pB->playTurn(5,6);
    pW->playTurn(5,7);
    pB->playTurn(4,5);
    pW->playTurn(3,5);
    pB->playTurn(4,4);
    pW->playTurn(4,3);
    pB->playTurn(5,3);
    pW->playTurn(6,3);

    game->getBoard()->printScores();

    delete game;

    return 0;
}