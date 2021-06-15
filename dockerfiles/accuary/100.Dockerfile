FROM smoosh

ADD --chown=opam:opam tests tests

RUN opam config exec -- make -C libdash/test test && \
    make -C src/ test && \
    TEST_DEBUG=1 make -C tests/ test && \
    echo ======================================================================== \
    && src/smoosh --version \
    && echo ALL TESTS PASSED >&2

ADD --chown=opam:opam modernish modernish

# TODO broken?
#RUN yes n | modernish/install.sh -s smoosh >modernish.log ; \\
#    cat modernish.log

ENTRYPOINT [ "opam", "config", "exec", "--", "bash" ]


# Comentário por Mateus Medeiros
# SM09 linha 1
# SM05 linha 14
# SM01