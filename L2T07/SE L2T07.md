# SE L2T07

1. A protocol is a set of rules or guidelines that dictate how something should be done. It is often used in the context of communication between computer systems, where protocols define the format and sequence of messages exchanged between devices.
    
    In general, protocols provide a standardized way for different entities to interact with each other in a consistent and reliable manner. They ensure that all parties involved in a process or transaction follow the same set of rules, which can help to prevent errors and misunderstandings.
    
2. HTTP (Hypertext Transfer Protocol) is built on top of the TCP (Transmission Control Protocol). TCP is a transport-layer protocol that provides reliable and ordered delivery of data between two endpoints, while HTTP is an application-layer protocol that defines how web browsers and servers communicate over the internet. When a client sends an HTTP request to a server, TCP ensures that the request is transmitted correctly and in the proper order. Once the server receives the request, it sends an HTTP response back to the client, which is also transmitted using TCP.
3. If an HTTP request is successful, the status code of the response will be in the 2xx range. The most commonly used success status code is 200, which indicates that the request was successfully processed by the server and that the response contains the requested information. Other possible success codes include 201 (Created), 204 (No Content), 206 (Partial Content), and others, each of which has a specific meaning and use case. It's worth noting that even if a request is successful, the response may contain other information or metadata in addition to the requested content, such as headers or cookies.
4. A stateless protocol is a type of protocol that does not maintain any information about the previous interactions between a client and a server. This means that each request from the client is treated as an independent transaction, and the server does not keep track of any session or context information between requests. HTTP (Hypertext Transfer Protocol) is a stateless protocol, which means that each request from a client to a server is treated as a separate transaction, with no knowledge of any previous requests. This is why when you access a website, every new page you request requires a new HTTP request, even if it's from the same website.
5. b. image/jpeg
c. text/javascript
e. image/psd
f. text/calendar
    
    The invalid MIME types are:
    
    a. text/time (There is no MIME type called "text/time".)
    d. text/jsx (Although JSX is used in web development, there is no official MIME type for it.)
    
6. If a server does not allow a client permission to request a specific resource, the status message that the client can expect to receive is "403 Forbidden".
    
    The HTTP status code 403 indicates that the server understands the request but refuses to authorize it. This can happen if the client doesn't have the necessary authentication credentials to access the resource, or if the client's credentials are not sufficient for the requested resource.
    
    For example, if a client tries to access a protected file on a server without the proper authentication credentials, the server may respond with a 403 Forbidden status message to indicate that the request was understood but access to the requested resource is forbidden.