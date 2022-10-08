a ="  **\n *  *\n*    *\n******\n*    *".split("\n")
b ="***\n*   *\n***\n*   *\n***\n".split("\n")
c =" **** \n*    *\n*     \n*    *\n **** ".split("\n")
d ="***\n*  *\n*   *\n*  *\n***".split("\n")
e ="******\n*\n******\n*\n******".split("\n")
f ="******\n*\n******\n*\n*".split("\n")
g ="******\n*     *\n*\n*   ****\n*****  *".split("\n")
h ="*     *\n*     *\n*******\n*     *\n*     *".split("\n")
i ="*******\n   *   \n   *   \n   *   \n*******".split("\n")
j ="*******\n   *    \n   *    \n*  *    \n****  ".split("\n")
k ="*  *\n* * \n**  \n* * \n*  *".split("\n")
l ="*    \n*    \n*    \n*    \n*****".split("\n")
m ="*     *\n* * * *\n*  *  *\n*     *\n*     *".split("\n")
n ="*     *\n* *   *\n*  *  *\n*   * *\n*     *".split("\n")
o ="   *   \n *   * \n*     *\n *   *\n   *   ".split("\n")
p ="**** \n*   *\n****\n*    \n*    ".split("\n")
q =" ****\n*   *\n ****\n    *\n    *".split("\n")
r ="**** \n*   *\n**** \n**   \n*  * ".split("\n")
s =" *** \n*    \n *** \n    *\n *** ".split("\n")
t ="*******\n   *   \n   *   \n   *   \n   *   ".split("\n")
u ="*     *\n*     *\n*     *\n*     *\n  *** ".split("\n")
v = "*       *\n *     * \n  *   *  \n   * *   \n    *    ".split("\n")
w ="*       *       *\n *     * *     * \n  *   *   *   *  \n   * *     * *   \n    *       *    ".split("\n")
x ="*   *\n * *  \n  *   \n * *  \n*   *\n"
y ="*   *\n * * \n  *   \n  *   \n  *  ".split("\n")
z ="*******\n    *  \n   *   \n *     \n*******".split("\n")

word = input("enter a word = ")
letters = []
for i in range(len(word)):
    letters.append(word[i])

for i in range(len(letters)):
    for j in range(5):
        print(letters[i])
