using System.Collections.Generic;

namespace ConsoleApplication
{
    // http://stackoverflow.com/questions/16730753/the-type-t-must-be-a-non-nullable-value-type-in-order-to-use-it-as-parameter/16730802
    class RedBlackTree
    // <T> where T: struct
    {
        class RedBlackTreeNode
        {
            enum RedBlackTreeNodeColor
            {
                Black,
                Red
            }

            RedBlackTreeNode()
            {
                this.color = RedBlackTreeNodeColor.Black;
                this.t = null;
            }

            RedBlackTreeNodeColor color;
            int? t;
        }

        RedBlackTree()
        {
        }

        void Insert(int t)
        {
            this.list.Add(t);
        }

        int Find(int t)
        {
            return this.list.Find(x => x == t);
        }

        List<int> list;
    }
}
