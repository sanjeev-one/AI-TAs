import streamlit as st
import openai
import os

# Set your OpenAI API key

openai.api_key = os.getenv("OPENAI_API_KEY")

conversation = []


# Streamlit app
def main():
    st.title("AI TAs for CS201")

    # Input for URL
    url = st.text_input(
        "Enter the text of your APT",
        """PathSum APT
Class

    public class PathSum {
        public int hasPath(int target, TreeNode tree){
            // replace with working code
            return 0;
        }
    }
Problem Statement
Write a method that returns 1 if there is a root-to-leaf path whose node values sum to target and returns 0 if there is no such root-to-leaf path.
For example, in the tree below there are exactly four root-to-leaf paths. The sums on these paths are 27, 22, 26, 18, so hasPathSum(22,tree) will return 1 for the tree shown and hasPathSum(32,tree) will return 0 for the tree shown.

Note that an empty tree will always return 0, regardless of the value of target. Similarly, a tree with exactly one node will result in returning 1 if target is the value in the node, and zero otherwise.



The TreeNode class will be accessible when your method is tested.


  public class TreeNode {
      int info;
      TreeNode left;
      TreeNode right;
      TreeNode(int x){
          info = x;
      }
      TreeNode(int x, TreeNode lNode, TreeNode rNode){
          info = x;
   	  left = lNode;
          right = rNode;
      }
  }

In the descriptions below, the input for a tree is shown as a pre-order traversal with null nodes labeled with th character/string 'x'. For example the tree here:


is characterized by the pre-order string 8, 4, x, 6, x, x, 12, 10, x, x, 15, x, x

Constraints
The trees will have at most 1,024 nodes
The trees will have a height at most 1,024
Examples
target = 5
tree = {5,x,x} 
Returns 1, there is a path whose sum is target
target = 4
tree = {5,x,x}

Returns 0, there is no path that sums to 5
target = 18 
tree = {5, 4, 11, 7, x, x, 2, x, x, x, 8, 13, x, x, 4, x, 1, x, x}
Returns 1, this is the tree diagrammed above

target = 20
tree = {5, 4, 11, 7, x, x, 2, x, x, x, 8, 13, x, x, 4, x, 1, x, x}
Returns 0, this is the tree diagrammed above

Creative Commons License
This work is copyright © Owen Astrachan and is licensed under a Creative Commons Attribution-Share Alike 3.0 Unported License.""",
    )

    # Input for OpenAI prompt
    prompt = """You are a progressive, conversational tutor. 
    You take students step by step through the coding question (APT) they’re working on, teaching them why to take each step, or asking them questions about what they want to do and then giving them feedback and steering the conversation toward completing the question. The student is in a intro to data structures course and they’re coding in Java. Don’t write code for them but answer questions and help them solve the whole problem
.never write out code for them. DO NOT WRITE CODE FOR THE STUDENT. DO NOT WRITE CODE FOR THE STUDENT.
"""

    # Input for OpenAI code
    code = st.text_input(
        "Enter your APT progress",
        """
public class PathSum {
    public int hasPath(int target, TreeNode tree) {
        // replace with working code
        if (tree == null) {
            return 0;
        }

        if (tree.info == target) {
            return 1;
        }

        return hasPath(target - tree.info, tree.left) + hasPath(target + tree.info, tree.right);

    }
}""",
    )

    if st.button("Help me"):
        # Scrape the URL
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, "html.parser")
        # scraped_data = soup.get_text()

        # Display the scraped data
        # st.write(scraped_data)
        conversation.insert(0, {"role": "system", "content": prompt})
        conversation.append(
            {
                "role": "user",
                "content": f"This is what the student is trying to do: \n\n {url}",
            }
        )

        conversation.append(
            {
                "role": "user",
                "content": f"This is what the student has so far: \n\n {code}",
            }
        )
        # Query OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            temperature=0,
        )
        conversation.append(
            {"role": "assistant", "content": response.choices[0].message["content"]}
        )

        # Display the OpenAI response
        st.write(response.choices[0].message["content"])


if __name__ == "__main__":
    main()
