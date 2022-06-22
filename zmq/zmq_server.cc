//zmqserver.cpp
 
#include <string.h>
#include <unistd.h>
#include <string>
#include <iostream>
#include <zmq.h>
#include <vector>
#include <utility>
#include <thread>
 
int main() {
 
    void *context = zmq_init(3);

    void * socket_rep = zmq_socket (context, ZMQ_REP);
    zmq_bind(socket_rep, "tcp://127.0.0.1:35820");

    void * socket_pub = zmq_socket (context, ZMQ_PUB);
    zmq_bind(socket_pub, "tcp://127.0.0.1:35821");
 
    void * socket_req = zmq_socket (context, ZMQ_REQ);
    zmq_bind(socket_req, "tcp://127.0.0.1:35822");

    std::cout << "Server is starting..." << std::endl;


    auto th1 = std::make_unique<std::thread> ([socket_rep](){
      while (true) {
        zmq_msg_t msg;
        int rc = zmq_msg_init_size (&msg, 128);
        /* Block until a message is available to be received from socket */
        rc = zmq_msg_recv (&msg, socket_rep, 0);
        std::cout << "reponse Come from client." << (char*)zmq_msg_data(&msg)<< std::endl;
 
        const char * sz = "i am zmq server:35280!";
        memcpy(zmq_msg_data(&msg), sz, strlen(sz));
        zmq_msg_send(&msg, socket_rep, 0);
      } 

    });    
    

    auto th2 = std::make_unique<std::thread> ([socket_pub](){
      while (true) {
        zmq_msg_t msg;
        int rc = zmq_msg_init_size (&msg, 128);
 
        // do some work
        sleep(1);
 
        const char * sz = "i am zmq server 35281!";
        memcpy(zmq_msg_data(&msg), sz, strlen(sz));
        zmq_msg_send(&msg, socket_pub, 0);
      } 

    });    

    auto th3 = std::make_unique<std::thread> ([socket_req](){
      while (true) {
        zmq_msg_t msg;
        int rc = zmq_msg_init_size (&msg, 128);

        const char * sz = "i am zmq server:35282!";
        memcpy(zmq_msg_data(&msg), sz, strlen(sz));
        std::cout << "send:" << std::endl;
        zmq_msg_send(&msg, socket_req, 0);
        std::cout << "send done:" << std::endl;
        zmq_msg_close(&msg);

        zmq_msg_init(&msg);
        rc = zmq_msg_recv (&msg, socket_req, 0);
        std::cout << "request Come from client." << (char*)zmq_msg_data(&msg)<< std::endl;
        zmq_msg_close(&msg);
      } 

    });    

    th1->join();
    th2->join();
    th3->join();
 
    return 0;
}
