#-------------------------------------------------
#
# Project created by QtCreator 2016-02-03T09:06:08
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = SampleProgram
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    status.cpp

HEADERS  += mainwindow.h \
    status.h

FORMS    += mainwindow.ui \
    status.ui

OTHER_FILES += \
    biogassymbol.jpg

RESOURCES += \
    resourcefiles.qrc
