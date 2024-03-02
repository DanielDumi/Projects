#include <iostream>
#include <algorithm>

using namespace std;


enum suits {Diamond, Clubs, Heart, Spade};

int s1 = 0, s2 = 0, no_cards1 = 26, no_cards2 = 26, st1 = 0, st2 = 0;
int _no_card_used1=0, _no_card_used2=0;
int pl1=0;


class  card{

protected:

    int rank;
    suits suit;

public:
    //getters
    int get_rank();
    suits get_suit();

    //constructors
    card(){
        rank = 11;
        suit = Clubs;

    }
    card(suits sts, int rnk){

        suit = sts;
        rank = rnk;

    }

    //friend function
    friend ostream& operator<<(ostream&, card&);
    friend bool operator<(card&, card&);
    friend bool operator>(card&, card&);
    friend bool operator==(card&, card&);

};

//defining friend functions
ostream& operator<<(ostream& out, card& rnk_card){
    switch(rnk_card.rank)
    {
        case 11: out <<"Ace"; break;
        case 12: out <<"Jack"; break;
        case 13: out <<"Queen"; break;
        case 14: out <<"King"; break;
        default: out <<rnk_card.rank; break;

    }
    switch (rnk_card.suit) {

        case Diamond:out << " of Diamonds"; break;
        case Clubs:out << " of Clubs"; break;
        case Spade:out <<" of Spade"; break;
        case Heart:out <<" of Heart"; break;

    }
    return out;


}

bool operator<(card& c, card& c1){

    return c.rank < c1.rank;
}
bool operator>(card& c, card& c1){

    return c.rank > c1.rank;
}
bool operator==(card& c, card& c1){

    return c.rank == c1.rank;

}


class deck{

protected:
    card cards[52];
    int top;
public:
    //constructor
    deck(){

        top = 0;
        for(int i = 2; i<=14; i++){
            card c_1(Diamond, i);
            card c_2(Spade, i);
            card c_3(Heart, i);
            card c_4(Clubs, i);
            cards[top++] = c_1;
            cards[top++] = c_2;
            cards[top++] = c_3;
            cards[top++] = c_4;
        }


    }

    //functions
    void shuffle(){

        random_shuffle(cards, cards + 52);

    }


    bool empty(){

        return top <= 0;

    }
    card draw(){

        if(empty())
            cout<<"The deck is empty";
        return cards[top--];
    }


};

class player{

protected:
    int no_cards_remained;
    card hand[3];
    int u_score;
    int discard;

public:
    player(deck&,int);
    card draw();
    void increase_score(int);
    void modify_no_cards(int);
    int score();
    int num_cards();
    void replace(deck&);


};
player ::player(deck& u_deck, int nr_card) {

    u_score = 0;
    no_cards_remained = nr_card;

    for(int i = 0; i < 3; i++){
        hand[i] = u_deck.draw();

        if (pl1==0) _no_card_used1++;
        else _no_card_used2++;

        discard = 0;
    }

}
card player::draw() {

    discard = rand() % 3;
    return hand[discard];

}
void player::increase_score(int no) {

    u_score += no;

}
void player::modify_no_cards(int nr1) {

    no_cards_remained = no_cards_remained + nr1;

}
int player::num_cards() {

    return no_cards_remained;

}
int player::score() {

    return u_score;

}
void player::replace(deck& u_deck) {

    if (pl1==1)
    {
        if(_no_card_used1 < no_cards1 ) {
            hand[discard] = u_deck.draw();
            _no_card_used1++;
        }

    }
    else
    {
        if(_no_card_used2 < no_cards2) {
            hand[discard] = u_deck.draw();
            _no_card_used2++;
        }
    }


}
void Main_menu()
{
    cout << " ----------------------------------------\n";
    cout << " \t\t MAIN MENU \t \n ";
    cout << " ----------------------------------------\n";
    cout << " 1. Start Games\n";
    cout << " 2. View last results\n";
    cout << " 3. Reload \n";
    cout << " 4. Exit \n";
}
void Game(){

    _no_card_used1=0;
    _no_card_used2=0;

    deck card_deck1;

    card_deck1.shuffle();

    pl1=1;
    player p1(card_deck1,no_cards1);

    pl1=0;
    player p2(card_deck1,no_cards2);

    do {

        card c1 = p1.draw();
        cout << "Player 1 draws:" << c1 << "\n";

        card c2 = p2.draw();
        cout << "Player 2 draws:" << c2 << "\n";

        if (c1 == c2) {

            p1.increase_score(1);
            p2.increase_score(1);
            cout << "War\n";

        } else if (c1 > c2) {
            p1.increase_score(2);
            p1.modify_no_cards(1);
            p2.modify_no_cards(-1);
            cout << "p1 takes the cards\n";

        } else {
            p2.increase_score(2);
            p2.modify_no_cards(1);
            p1.modify_no_cards(-1);
            cout << "p2 takes the cards\n";

        }

        pl1=1;
        p1.replace(card_deck1);

        pl1=0;
        p2.replace(card_deck1);


    } while (!card_deck1.empty());

    s1 = p1.score();
    s2 = p2.score();
    no_cards1 = p1.num_cards();
    no_cards2 = p2.num_cards();

    cout << "p1 score:" << s1 << "\n";
    cout << "p2 score:" << s2 << "\n";
    cout <<"\n";
    cout << "p1 no of cards remained:" << no_cards1 << "\n";
    cout << "p2 no of cards remained:" << no_cards2 << "\n";
    cout <<"Nr card used of player 1: "<< _no_card_used1 << "\n";
    cout <<"Nr card used of player 2: "<< _no_card_used2 << "\n";
    st1 = st1 + s1;
    st2 = st2 + s2;
    cout << "p1 total score:" << st1 << "\n";
    cout << "p2 total score:" << st2 << "\n";

}
void LastScore()
{   cout <<"\n";
    cout <<"...................................................";
    cout <<"\n";
    cout << "p1 score:" << s1 << "\n";
    cout << "p2 score:" << s2 << "\n";
    cout <<"...................................................";
    cout <<"\n";
    cout << "p1 no of cards remained:" << no_cards1 << "\n";
    cout << "p2 no of cards remained:" << no_cards2 << "\n";


}
int main() {


    Main_menu();
    int your_choice;
    string confirm;

    do
    {

        cout << "Enter your choice(1-4):";
        cin >> your_choice;

        switch (your_choice)
        {
            case 1: Game(); break;
            case 2: LastScore(); break;
            case 3: Main_menu(); break;
            case 4: return 0; break;
            default: cout << "Unknown key\n"; break;
        }

        cout << "Press y or Y to continue:";
        cin >> confirm;

    } while (confirm == "y" || confirm == "Y");

    return 0;
}