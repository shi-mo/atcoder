import std.algorithm;
import std.conv;
import std.stdio;
import std.string;

void solve(long N, long[] d){

}

// Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
int main(){
    auto input = stdin.byLine.map!split.joiner;

    long N;
    N = input.front.to!long;
    input.popFront;

    long[] d = new long[](cast(size_t) (N));
    foreach (i; 0 .. cast(size_t) (N)) {
        d[i] = input.front.to!long;
        input.popFront;
    }

    solve(N, d);
    return 0;
}
