

mcp_tools_list = []
mcp_prompts_list = []

if __name__ == "__main__":
    print("welcome to mcp creator")
    mcp_name = input("insert the name of your mcp server: ")

    mcp_tools = int(input("how many tools you want for your mcp server: "))
    mcp_prompts = int(input("how many prompts you want for your mcp server: "))

    for i in range(mcp_tools):
        name_tool = input("insert the name of the tool: ")
        mcp_tools_list.append(name_tool)

    for i in range(mcp_prompts):
        name_prompt = input("insert the name of function for the prompt: ")
        mcp_prompts_list.append(name_prompt)

    filename = mcp_name + ".py"
    with open(filename,"w") as mcp_final_filename:
        mcp_final_filename.write("from mcp.server.fastmcp import FastMCP  \n \n")
        mcp_final_filename.write("mcp=FastMCP(\"{}\") \n \n".format(mcp_name))

        for item in mcp_tools_list:
            mcp_final_filename.write("@mcp.tool() \n")
            mcp_final_filename.write("def {}(): \n".format(item))
            mcp_final_filename.write("\tpass \n \n")

        for item in mcp_prompts_list:
            mcp_final_filename.write("@mcp.prompt() \n")
            mcp_final_filename.write("def {}(): \n".format(item))
            mcp_final_filename.write("\tpass \n \n")



