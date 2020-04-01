<html>
<head>
<title>Hello</title>
</head>
<body>
<h1>
<%
String userName = request.getParameter("userName");
if(userName == null || userName.trim().equals(""))
    out.print("Hello world!");
else
    out.print("Hello " + userName + "!");
%>
</h1>
<form action="/hello" method="post">
Name: <input type="text" name="userName" /><br/>
<input type="submit" value="Submit">
</form>
</body>
</html>