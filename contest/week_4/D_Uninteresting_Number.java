import java.util.*

fun main() {
    val sc = Scanner(System.`in`)
    val t = sc.nextInt()

    repeat(t) {
        val s = sc.next()
        var contains3 = false
        var sum = 0
        for (c in s) {
            val d = c - '0'
            if (d == 3) contains3 = true
            sum += d
        }
        if (contains3 || sum % 9 == 0) println("YES") else println("NO")
    }
}