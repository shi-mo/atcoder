import std.algorithm;
import std.conv;
import std.stdio;
import std.string;

void solve(long a, long b, long c, string s){
    writefln("%d %s", a+b+c, s);
}

int main(){
    auto input = stdin.byLine.map!split.joiner;

    long a;
    a = input.front.to!long;
    input.popFront;

    long b;
    b = input.front.to!long;
    input.popFront;

    long c;
    c = input.front.to!long;
    input.popFront;

    string s;
    s = input.front.to!string;
    input.popFront;

    solve(a, b, c, s);
    return 0;
}
