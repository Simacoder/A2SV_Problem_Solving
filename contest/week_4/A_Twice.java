import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val t = br.readLine().toInt()
    val sb = StringBuilder()

    repeat(t) {
        val n = br.readLine().toInt()
        val st = StringTokenizer(br.readLine())

        val freq = IntArray(n + 1)

        repeat(n) {
            val x = st.nextToken().toInt()
            freq[x]++
        }

        var score = 0
        for (f in freq) {
            score += f / 2
        }

        sb.append(score).append('\n')
    }

    print(sb)
}