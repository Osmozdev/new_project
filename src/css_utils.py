import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def navigation_bar():
    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True)

    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
      <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Tantan Dev Place</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Courses</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Art & Creations</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank"> Osmoz <3</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Data Science and Analytics projects</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank"> Contact me !</a>
          </li>
        </ul>
      </div>
    </nav>
    """, unsafe_allow_html=True)
