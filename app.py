import streamlit as st
from PROGRAM import kruskal, prim

st.title("Comparative Analysis of Kruskal's and Prim's Algorithms")
if st.button("Generate MST"):
    n = 7
    edges = [
        (7,0,1),
        (5,0,3),
        (8,1,2),
        (9,1,3),
        (7,1,4),
        (5,2,4),
        (15,3,4),
        (6,3,5),
        (8,4,5),
        (9,4,6),
        (11,5,6)
    ]
    adj = {}
    for w,u,v in edges:
        adj.setdefault(u,[]).append((v,w))
        adj.setdefault(v,[]).append((u,w))
    k_mst,k_cost = kruskal(n,edges[:])
    p_mst,p_cost = prim(n,adj)
    st.subheader("Kruskal's Algorithm")
    st.write("MST Edges:", k_mst)
    st.write("Total Cost:", k_cost)

    st.subheader("Prim's Algorithm")
    st.write("MST Edges:", p_mst)
    st.write("Total Cost:", p_cost)
