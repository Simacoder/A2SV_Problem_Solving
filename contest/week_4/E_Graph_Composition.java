import java.util.*

class DSU(n: Int) {
    private val parent = IntArray(n + 1) { it }
    fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }
    fun union(x: Int, y: Int) {
        val px = find(x)
        val py = find(y)
        if (px != py) parent[px] = py
    }
    fun countComponents(): Int {
        val s = mutableSetOf<Int>()
        for (i in 1..parent.lastIndex) s.add(find(i))
        return s.size
    }
}

fun main() {
    val sc = Scanner(System.`in`)
    val t = sc.nextInt()

    repeat(t) {
        val n = sc.nextInt()
        val m1 = sc.nextInt()
        val m2 = sc.nextInt()

        val dsuF = DSU(n)
        repeat(m1) {
            val u = sc.nextInt()
            val v = sc.nextInt()
            dsuF.union(u, v)
        }

        val dsuG = DSU(n)
        repeat(m2) {
            val u = sc.nextInt()
            val v = sc.nextInt()
            dsuG.union(u, v)
        }

        val cF = dsuF.countComponents()
        val cG = dsuG.countComponents()
        println(kotlin.math.abs(cF - cG))
    }
}