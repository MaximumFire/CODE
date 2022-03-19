local a = io.read("*n")

table = {}

--[[Fib = function (n)
    if n <= 1 then
        return n
    else           
        for i = 1,#table,1
        do
            table[n] = Fib(n-1) + Fib(n-2)
            return table[n]
        end
    end
end--]]
table[1] = 1

b = table[1]

io.write(b)