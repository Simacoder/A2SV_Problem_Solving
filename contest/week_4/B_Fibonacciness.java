import java.util.*

fun main() {
    val sc = Scanner(System.`in`)
    val t = sc.nextInt()

    repeat(t) {
        val a1 = sc.nextInt()
        val a2 = sc.nextInt()
        val a4 = sc.nextInt()
        val a5 = sc.nextInt()

        val candidates = listOf(
            a1 + a2,      // f1
            a4 - a2,      // f2
            a5 - a4       // f3
        )

        var maxScore = 1

        // Check if Fibonacciness 3 is possible
        if (candidates[0] == candidates[1] && candidates[1] == candidates[2]) {
            maxScore = 3
        } else {
            // Check if Fibonacciness 2 is possible
            if (candidates[0] == candidates[1] || candidates[0] == candidates[2] || candidates[1] == candidates[2]) {
                maxScore = 2
            }
        }

        println(maxScore)
    }
}