import java.util.*

fun main() {
    val sc = Scanner(System.`in`)
    val t = sc.nextInt()

    repeat(t) {
        val n = sc.nextInt()
        val m = sc.nextInt()
        val k = sc.nextInt()

        val a = IntArray(m) { sc.nextInt() }
        val known = mutableSetOf<Int>()
        repeat(k) { known.add(sc.nextInt()) }

        val unknownCount = n - known.size
        val unknownQuestion = (1..n).firstOrNull { it !in known }

        val result = StringBuilder()

        when {
            unknownCount == 0 -> {
                repeat(m) { result.append('1') }
            }
            unknownCount == 1 -> {
                for (ai in a) {
                    if (ai == unknownQuestion) result.append('1')
                    else result.append('0')
                }
            }
            else -> {
                repeat(m) { result.append('0') }
            }
        }

        println(result)
    }
}