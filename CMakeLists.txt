CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT})

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    zimg
    SOURCE_DIR ${CMAKE_SOURCE_DIR}
    PREFIX zimg
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${CMAKE_SOURCE_DIR}/configure
        --prefix=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
    BUILD_COMMAND make ${make_args}
)

# Necessary so REZ can create a `make install` target
rez_install_files(
    ${CMAKE_SOURCE_DIR}/ChangeLog
    DESTINATION .
)
