import std.algorithm;
import std.conv;
import std.stdio;
import std.string;

void solve(long N, long A, long B){

}

// Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
int main(){
    auto input = stdin.byLine.map!split.joiner;

    long N;
    N = input.front.to!long;
    input.popFront;

    long A;
    A = input.front.to!long;
    input.popFront;

    long B;
    B = input.front.to!long;
    input.popFront;

    solve(N, A, B);
    return 0;
}