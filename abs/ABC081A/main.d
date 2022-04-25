import std.regex;
import std.stdio;

int main(){
    string s = stdin.readln();
    s = s.replaceAll(regex(r"[0 \n]"), "");
    writeln(s.length);

    return 0;
}
