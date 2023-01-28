## This will be a makefile for the service

## TODO make a ./config executable script and two make targets: make and make install:
# https://thoughtbot.com/blog/the-magic-behind-configure-make-make-install

## how to detect os (put this in a config script?):
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # ...
elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Mac OSX
elif [[ "$OSTYPE" == "cygwin" ]]; then
        # POSIX compatibility layer and Linux environment emulation for Windows
elif [[ "$OSTYPE" == "msys" ]]; then
        # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
elif [[ "$OSTYPE" == "win32" ]]; then
        # I'm not sure this can happen.
elif [[ "$OSTYPE" == "freebsd"* ]]; then
        # ...
else
        # Unknown.
fi

## how to execute cmd checking/handling:
##! pip is pip3 now?
normal_target:
   if gcc -o main main.c; then \
      echo succeeded; \
   else \
      echo compilation failed; \
      gcc -o ...; \
   fi