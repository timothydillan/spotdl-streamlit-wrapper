# run by cd'ing to this folder, and do: streamlit run spotify.py
import streamlit as st
from os import path, popen


def main():
    st.write("# Spotify Downloader")

    folder = st.text_input('Input folder directory:')

    # Check whether the directory entered is not empty.
    if len(folder) > 1 and len(folder.strip()) > 0:
        # If the path entered is not a folder or if it isn't a valid directory,
        if not path.exists(folder) or not path.isdir(folder):
            # Show an error message.
            st.write("That was not a valid folder. Re-enter a valid directory path.")
        # else, if the path does exists,
        else:
            # Show a message
            st.write("Will download your songs to: " + folder)

        # And ask for input.
        song = st.text_input('Input song name/track url/album url:')

        # If the song isn't empty,
        if len(song) > 0 and len(song.strip()) > 0:
            # Download the song.
            download(folder, song)


def download(path, song):
    st.write("## Processing... Please wait...")
    st.write("### Once the download has been completed, a message will be shown.")
    stream = popen(f"spotdl -o {path} '{song}'")
    # The spotdl will usually output 100% once it's done downloading something. 
    while "100%" not in str(stream.read()):
        pass
    # So once it's done downloading something, show a download done message.
    st.markdown("<h2 style='color: #4BB543;'>Download done!</h2>",
                unsafe_allow_html=True)
    
# only run the main() function when this module is executed directly.
if __name__ == '__main__':
    main()
