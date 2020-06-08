/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 4.8.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QDoubleSpinBox>
#include <QtGui/QFrame>
#include <QtGui/QGroupBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLCDNumber>
#include <QtGui/QLabel>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QPushButton>
#include <QtGui/QSlider>
#include <QtGui/QSpacerItem>
#include <QtGui/QStatusBar>
#include <QtGui/QToolBar>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QLabel *label;
    QPushButton *pushButton_on;
    QLCDNumber *lcdNumber;
    QLabel *label_9;
    QGroupBox *groupBox_alr_2;
    QFrame *frame_5;
    QSlider *horizontalSlider_alr_3;
    QFrame *line_4;
    QLabel *label_16;
    QDoubleSpinBox *doubleSpinBox_alr_3;
    QLabel *label_17;
    QLabel *label_alr_3;
    QLabel *label_18;
    QCheckBox *checkBox_alr_3;
    QGroupBox *groupBox_alr;
    QFrame *frame_3;
    QWidget *widget;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QDoubleSpinBox *doubleSpinBox_alr;
    QLabel *label_11;
    QSlider *horizontalSlider_alr;
    QFrame *line_2;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_alr;
    QSpacerItem *horizontalSpacer;
    QLabel *label_13;
    QWidget *widget1;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_10;
    QCheckBox *checkBox_alr;
    QGroupBox *groupBox_alr_3;
    QFrame *frame_6;
    QSlider *horizontalSlider_alr_4;
    QFrame *line_5;
    QLabel *label_19;
    QDoubleSpinBox *doubleSpinBox_alr_4;
    QLabel *label_20;
    QLabel *label_alr_4;
    QLabel *label_21;
    QCheckBox *checkBox_alr_4;
    QGroupBox *groupBox_alr_4;
    QFrame *frame_7;
    QSlider *horizontalSlider_alr_5;
    QFrame *line_6;
    QLabel *label_22;
    QDoubleSpinBox *doubleSpinBox_alr_5;
    QLabel *label_23;
    QLabel *label_alr_5;
    QLabel *label_24;
    QCheckBox *checkBox_alr_5;
    QGroupBox *groupBox_alr_5;
    QFrame *frame_8;
    QSlider *horizontalSlider_alr_6;
    QFrame *line_7;
    QLabel *label_25;
    QDoubleSpinBox *doubleSpinBox_alr_6;
    QLabel *label_26;
    QLabel *label_alr_6;
    QLabel *label_27;
    QCheckBox *checkBox_alr_6;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(806, 660);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        label = new QLabel(centralWidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(160, 20, 78, 22));
        QFont font;
        font.setPointSize(14);
        font.setBold(true);
        font.setWeight(75);
        label->setFont(font);
        pushButton_on = new QPushButton(centralWidget);
        pushButton_on->setObjectName(QString::fromUtf8("pushButton_on"));
        pushButton_on->setGeometry(QRect(480, 430, 85, 27));
        lcdNumber = new QLCDNumber(centralWidget);
        lcdNumber->setObjectName(QString::fromUtf8("lcdNumber"));
        lcdNumber->setGeometry(QRect(90, 430, 64, 23));
        label_9 = new QLabel(centralWidget);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(10, 435, 67, 17));
        QFont font1;
        font1.setPointSize(11);
        font1.setBold(true);
        font1.setWeight(75);
        label_9->setFont(font1);
        groupBox_alr_2 = new QGroupBox(centralWidget);
        groupBox_alr_2->setObjectName(QString::fromUtf8("groupBox_alr_2"));
        groupBox_alr_2->setGeometry(QRect(26, 230, 171, 151));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(groupBox_alr_2->sizePolicy().hasHeightForWidth());
        groupBox_alr_2->setSizePolicy(sizePolicy);
        frame_5 = new QFrame(groupBox_alr_2);
        frame_5->setObjectName(QString::fromUtf8("frame_5"));
        frame_5->setGeometry(QRect(4, 30, 154, 120));
        sizePolicy.setHeightForWidth(frame_5->sizePolicy().hasHeightForWidth());
        frame_5->setSizePolicy(sizePolicy);
        frame_5->setFrameShape(QFrame::StyledPanel);
        frame_5->setFrameShadow(QFrame::Raised);
        frame_5->setLineWidth(1);
        horizontalSlider_alr_3 = new QSlider(frame_5);
        horizontalSlider_alr_3->setObjectName(QString::fromUtf8("horizontalSlider_alr_3"));
        horizontalSlider_alr_3->setGeometry(QRect(9, 41, 131, 29));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(horizontalSlider_alr_3->sizePolicy().hasHeightForWidth());
        horizontalSlider_alr_3->setSizePolicy(sizePolicy1);
        horizontalSlider_alr_3->setMaximum(100);
        horizontalSlider_alr_3->setSingleStep(0);
        horizontalSlider_alr_3->setOrientation(Qt::Horizontal);
        horizontalSlider_alr_3->setTickPosition(QSlider::NoTicks);
        line_4 = new QFrame(frame_5);
        line_4->setObjectName(QString::fromUtf8("line_4"));
        line_4->setGeometry(QRect(9, 68, 136, 16));
        sizePolicy1.setHeightForWidth(line_4->sizePolicy().hasHeightForWidth());
        line_4->setSizePolicy(sizePolicy1);
        line_4->setFrameShape(QFrame::HLine);
        line_4->setFrameShadow(QFrame::Sunken);
        label_16 = new QLabel(frame_5);
        label_16->setObjectName(QString::fromUtf8("label_16"));
        label_16->setGeometry(QRect(66, 12, 78, 16));
        sizePolicy1.setHeightForWidth(label_16->sizePolicy().hasHeightForWidth());
        label_16->setSizePolicy(sizePolicy1);
        QFont font2;
        font2.setPointSize(10);
        label_16->setFont(font2);
        label_16->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        doubleSpinBox_alr_3 = new QDoubleSpinBox(frame_5);
        doubleSpinBox_alr_3->setObjectName(QString::fromUtf8("doubleSpinBox_alr_3"));
        doubleSpinBox_alr_3->setGeometry(QRect(10, 8, 50, 27));
        sizePolicy1.setHeightForWidth(doubleSpinBox_alr_3->sizePolicy().hasHeightForWidth());
        doubleSpinBox_alr_3->setSizePolicy(sizePolicy1);
        doubleSpinBox_alr_3->setMaximumSize(QSize(50, 16777215));
        doubleSpinBox_alr_3->setAlignment(Qt::AlignCenter);
        doubleSpinBox_alr_3->setDecimals(1);
        doubleSpinBox_alr_3->setMaximum(5);
        doubleSpinBox_alr_3->setSingleStep(0.1);
        label_17 = new QLabel(frame_5);
        label_17->setObjectName(QString::fromUtf8("label_17"));
        label_17->setGeometry(QRect(72, 90, 72, 16));
        sizePolicy1.setHeightForWidth(label_17->sizePolicy().hasHeightForWidth());
        label_17->setSizePolicy(sizePolicy1);
        label_17->setFont(font2);
        label_17->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_alr_3 = new QLabel(frame_5);
        label_alr_3->setObjectName(QString::fromUtf8("label_alr_3"));
        label_alr_3->setEnabled(true);
        label_alr_3->setGeometry(QRect(10, 86, 35, 25));
        sizePolicy1.setHeightForWidth(label_alr_3->sizePolicy().hasHeightForWidth());
        label_alr_3->setSizePolicy(sizePolicy1);
        label_alr_3->setMinimumSize(QSize(0, 25));
        label_alr_3->setAutoFillBackground(false);
        label_alr_3->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(196, 193, 189);"));
        label_alr_3->setFrameShape(QFrame::StyledPanel);
        label_alr_3->setAlignment(Qt::AlignCenter);
        label_18 = new QLabel(groupBox_alr_2);
        label_18->setObjectName(QString::fromUtf8("label_18"));
        label_18->setGeometry(QRect(8, 6, 87, 17));
        sizePolicy1.setHeightForWidth(label_18->sizePolicy().hasHeightForWidth());
        label_18->setSizePolicy(sizePolicy1);
        label_18->setFont(font1);
        checkBox_alr_3 = new QCheckBox(groupBox_alr_2);
        checkBox_alr_3->setObjectName(QString::fromUtf8("checkBox_alr_3"));
        checkBox_alr_3->setGeometry(QRect(101, 6, 20, 21));
        sizePolicy1.setHeightForWidth(checkBox_alr_3->sizePolicy().hasHeightForWidth());
        checkBox_alr_3->setSizePolicy(sizePolicy1);
        groupBox_alr = new QGroupBox(centralWidget);
        groupBox_alr->setObjectName(QString::fromUtf8("groupBox_alr"));
        groupBox_alr->setEnabled(true);
        groupBox_alr->setGeometry(QRect(180, 490, 161, 151));
        frame_3 = new QFrame(groupBox_alr);
        frame_3->setObjectName(QString::fromUtf8("frame_3"));
        frame_3->setGeometry(QRect(4, 95, 154, 120));
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        frame_3->setLineWidth(1);
        widget = new QWidget(frame_3);
        widget->setObjectName(QString::fromUtf8("widget"));
        widget->setGeometry(QRect(8, 71, 138, 108));
        verticalLayout = new QVBoxLayout(widget);
        verticalLayout->setSpacing(5);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        doubleSpinBox_alr = new QDoubleSpinBox(widget);
        doubleSpinBox_alr->setObjectName(QString::fromUtf8("doubleSpinBox_alr"));
        doubleSpinBox_alr->setMaximumSize(QSize(50, 16777215));
        doubleSpinBox_alr->setAlignment(Qt::AlignCenter);
        doubleSpinBox_alr->setDecimals(1);
        doubleSpinBox_alr->setMaximum(5);
        doubleSpinBox_alr->setSingleStep(0.1);

        horizontalLayout->addWidget(doubleSpinBox_alr);

        label_11 = new QLabel(widget);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setFont(font2);
        label_11->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        horizontalLayout->addWidget(label_11);


        verticalLayout->addLayout(horizontalLayout);

        horizontalSlider_alr = new QSlider(widget);
        horizontalSlider_alr->setObjectName(QString::fromUtf8("horizontalSlider_alr"));
        horizontalSlider_alr->setMaximum(100);
        horizontalSlider_alr->setSingleStep(0);
        horizontalSlider_alr->setOrientation(Qt::Horizontal);
        horizontalSlider_alr->setTickPosition(QSlider::NoTicks);

        verticalLayout->addWidget(horizontalSlider_alr);

        line_2 = new QFrame(widget);
        line_2->setObjectName(QString::fromUtf8("line_2"));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);

        verticalLayout->addWidget(line_2);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_alr = new QLabel(widget);
        label_alr->setObjectName(QString::fromUtf8("label_alr"));
        label_alr->setEnabled(true);
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(label_alr->sizePolicy().hasHeightForWidth());
        label_alr->setSizePolicy(sizePolicy2);
        label_alr->setMinimumSize(QSize(0, 25));
        label_alr->setAutoFillBackground(false);
        label_alr->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(196, 193, 189);"));
        label_alr->setFrameShape(QFrame::StyledPanel);
        label_alr->setAlignment(Qt::AlignCenter);

        horizontalLayout_2->addWidget(label_alr);

        horizontalSpacer = new QSpacerItem(18, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        label_13 = new QLabel(widget);
        label_13->setObjectName(QString::fromUtf8("label_13"));
        label_13->setFont(font2);
        label_13->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        horizontalLayout_2->addWidget(label_13);


        verticalLayout->addLayout(horizontalLayout_2);

        widget1 = new QWidget(groupBox_alr);
        widget1->setObjectName(QString::fromUtf8("widget1"));
        widget1->setGeometry(QRect(6, 69, 115, 23));
        horizontalLayout_3 = new QHBoxLayout(widget1);
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        label_10 = new QLabel(widget1);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setFont(font1);

        horizontalLayout_3->addWidget(label_10);

        checkBox_alr = new QCheckBox(widget1);
        checkBox_alr->setObjectName(QString::fromUtf8("checkBox_alr"));

        horizontalLayout_3->addWidget(checkBox_alr);

        groupBox_alr_3 = new QGroupBox(centralWidget);
        groupBox_alr_3->setObjectName(QString::fromUtf8("groupBox_alr_3"));
        groupBox_alr_3->setGeometry(QRect(26, 60, 171, 151));
        sizePolicy.setHeightForWidth(groupBox_alr_3->sizePolicy().hasHeightForWidth());
        groupBox_alr_3->setSizePolicy(sizePolicy);
        frame_6 = new QFrame(groupBox_alr_3);
        frame_6->setObjectName(QString::fromUtf8("frame_6"));
        frame_6->setGeometry(QRect(4, 30, 154, 120));
        sizePolicy.setHeightForWidth(frame_6->sizePolicy().hasHeightForWidth());
        frame_6->setSizePolicy(sizePolicy);
        frame_6->setFrameShape(QFrame::StyledPanel);
        frame_6->setFrameShadow(QFrame::Raised);
        frame_6->setLineWidth(1);
        horizontalSlider_alr_4 = new QSlider(frame_6);
        horizontalSlider_alr_4->setObjectName(QString::fromUtf8("horizontalSlider_alr_4"));
        horizontalSlider_alr_4->setGeometry(QRect(9, 41, 131, 29));
        sizePolicy1.setHeightForWidth(horizontalSlider_alr_4->sizePolicy().hasHeightForWidth());
        horizontalSlider_alr_4->setSizePolicy(sizePolicy1);
        horizontalSlider_alr_4->setMaximum(100);
        horizontalSlider_alr_4->setSingleStep(0);
        horizontalSlider_alr_4->setOrientation(Qt::Horizontal);
        horizontalSlider_alr_4->setTickPosition(QSlider::NoTicks);
        line_5 = new QFrame(frame_6);
        line_5->setObjectName(QString::fromUtf8("line_5"));
        line_5->setGeometry(QRect(9, 68, 136, 16));
        sizePolicy1.setHeightForWidth(line_5->sizePolicy().hasHeightForWidth());
        line_5->setSizePolicy(sizePolicy1);
        line_5->setFrameShape(QFrame::HLine);
        line_5->setFrameShadow(QFrame::Sunken);
        label_19 = new QLabel(frame_6);
        label_19->setObjectName(QString::fromUtf8("label_19"));
        label_19->setGeometry(QRect(66, 12, 78, 16));
        sizePolicy1.setHeightForWidth(label_19->sizePolicy().hasHeightForWidth());
        label_19->setSizePolicy(sizePolicy1);
        label_19->setFont(font2);
        label_19->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        doubleSpinBox_alr_4 = new QDoubleSpinBox(frame_6);
        doubleSpinBox_alr_4->setObjectName(QString::fromUtf8("doubleSpinBox_alr_4"));
        doubleSpinBox_alr_4->setGeometry(QRect(10, 8, 50, 27));
        sizePolicy1.setHeightForWidth(doubleSpinBox_alr_4->sizePolicy().hasHeightForWidth());
        doubleSpinBox_alr_4->setSizePolicy(sizePolicy1);
        doubleSpinBox_alr_4->setMaximumSize(QSize(50, 16777215));
        doubleSpinBox_alr_4->setAlignment(Qt::AlignCenter);
        doubleSpinBox_alr_4->setDecimals(1);
        doubleSpinBox_alr_4->setMaximum(5);
        doubleSpinBox_alr_4->setSingleStep(0.1);
        label_20 = new QLabel(frame_6);
        label_20->setObjectName(QString::fromUtf8("label_20"));
        label_20->setGeometry(QRect(72, 90, 72, 16));
        sizePolicy1.setHeightForWidth(label_20->sizePolicy().hasHeightForWidth());
        label_20->setSizePolicy(sizePolicy1);
        label_20->setFont(font2);
        label_20->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_alr_4 = new QLabel(frame_6);
        label_alr_4->setObjectName(QString::fromUtf8("label_alr_4"));
        label_alr_4->setEnabled(true);
        label_alr_4->setGeometry(QRect(10, 86, 35, 25));
        sizePolicy1.setHeightForWidth(label_alr_4->sizePolicy().hasHeightForWidth());
        label_alr_4->setSizePolicy(sizePolicy1);
        label_alr_4->setMinimumSize(QSize(0, 25));
        label_alr_4->setAutoFillBackground(false);
        label_alr_4->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(196, 193, 189);"));
        label_alr_4->setFrameShape(QFrame::StyledPanel);
        label_alr_4->setAlignment(Qt::AlignCenter);
        label_21 = new QLabel(groupBox_alr_3);
        label_21->setObjectName(QString::fromUtf8("label_21"));
        label_21->setGeometry(QRect(8, 6, 87, 17));
        sizePolicy1.setHeightForWidth(label_21->sizePolicy().hasHeightForWidth());
        label_21->setSizePolicy(sizePolicy1);
        label_21->setFont(font1);
        checkBox_alr_4 = new QCheckBox(groupBox_alr_3);
        checkBox_alr_4->setObjectName(QString::fromUtf8("checkBox_alr_4"));
        checkBox_alr_4->setGeometry(QRect(101, 6, 20, 21));
        sizePolicy1.setHeightForWidth(checkBox_alr_4->sizePolicy().hasHeightForWidth());
        checkBox_alr_4->setSizePolicy(sizePolicy1);
        groupBox_alr_4 = new QGroupBox(centralWidget);
        groupBox_alr_4->setObjectName(QString::fromUtf8("groupBox_alr_4"));
        groupBox_alr_4->setGeometry(QRect(216, 229, 171, 151));
        sizePolicy.setHeightForWidth(groupBox_alr_4->sizePolicy().hasHeightForWidth());
        groupBox_alr_4->setSizePolicy(sizePolicy);
        frame_7 = new QFrame(groupBox_alr_4);
        frame_7->setObjectName(QString::fromUtf8("frame_7"));
        frame_7->setGeometry(QRect(4, 30, 154, 120));
        sizePolicy.setHeightForWidth(frame_7->sizePolicy().hasHeightForWidth());
        frame_7->setSizePolicy(sizePolicy);
        frame_7->setFrameShape(QFrame::StyledPanel);
        frame_7->setFrameShadow(QFrame::Raised);
        frame_7->setLineWidth(1);
        horizontalSlider_alr_5 = new QSlider(frame_7);
        horizontalSlider_alr_5->setObjectName(QString::fromUtf8("horizontalSlider_alr_5"));
        horizontalSlider_alr_5->setGeometry(QRect(9, 41, 131, 29));
        sizePolicy1.setHeightForWidth(horizontalSlider_alr_5->sizePolicy().hasHeightForWidth());
        horizontalSlider_alr_5->setSizePolicy(sizePolicy1);
        horizontalSlider_alr_5->setMaximum(100);
        horizontalSlider_alr_5->setSingleStep(0);
        horizontalSlider_alr_5->setOrientation(Qt::Horizontal);
        horizontalSlider_alr_5->setTickPosition(QSlider::NoTicks);
        line_6 = new QFrame(frame_7);
        line_6->setObjectName(QString::fromUtf8("line_6"));
        line_6->setGeometry(QRect(9, 68, 136, 16));
        sizePolicy1.setHeightForWidth(line_6->sizePolicy().hasHeightForWidth());
        line_6->setSizePolicy(sizePolicy1);
        line_6->setFrameShape(QFrame::HLine);
        line_6->setFrameShadow(QFrame::Sunken);
        label_22 = new QLabel(frame_7);
        label_22->setObjectName(QString::fromUtf8("label_22"));
        label_22->setGeometry(QRect(66, 12, 78, 16));
        sizePolicy1.setHeightForWidth(label_22->sizePolicy().hasHeightForWidth());
        label_22->setSizePolicy(sizePolicy1);
        label_22->setFont(font2);
        label_22->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        doubleSpinBox_alr_5 = new QDoubleSpinBox(frame_7);
        doubleSpinBox_alr_5->setObjectName(QString::fromUtf8("doubleSpinBox_alr_5"));
        doubleSpinBox_alr_5->setGeometry(QRect(10, 8, 50, 27));
        sizePolicy1.setHeightForWidth(doubleSpinBox_alr_5->sizePolicy().hasHeightForWidth());
        doubleSpinBox_alr_5->setSizePolicy(sizePolicy1);
        doubleSpinBox_alr_5->setMaximumSize(QSize(50, 16777215));
        doubleSpinBox_alr_5->setAlignment(Qt::AlignCenter);
        doubleSpinBox_alr_5->setDecimals(1);
        doubleSpinBox_alr_5->setMaximum(5);
        doubleSpinBox_alr_5->setSingleStep(0.1);
        label_23 = new QLabel(frame_7);
        label_23->setObjectName(QString::fromUtf8("label_23"));
        label_23->setGeometry(QRect(72, 90, 72, 16));
        sizePolicy1.setHeightForWidth(label_23->sizePolicy().hasHeightForWidth());
        label_23->setSizePolicy(sizePolicy1);
        label_23->setFont(font2);
        label_23->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_alr_5 = new QLabel(frame_7);
        label_alr_5->setObjectName(QString::fromUtf8("label_alr_5"));
        label_alr_5->setEnabled(true);
        label_alr_5->setGeometry(QRect(10, 86, 35, 25));
        sizePolicy1.setHeightForWidth(label_alr_5->sizePolicy().hasHeightForWidth());
        label_alr_5->setSizePolicy(sizePolicy1);
        label_alr_5->setMinimumSize(QSize(0, 25));
        label_alr_5->setAutoFillBackground(false);
        label_alr_5->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(196, 193, 189);"));
        label_alr_5->setFrameShape(QFrame::StyledPanel);
        label_alr_5->setAlignment(Qt::AlignCenter);
        label_24 = new QLabel(groupBox_alr_4);
        label_24->setObjectName(QString::fromUtf8("label_24"));
        label_24->setGeometry(QRect(8, 6, 87, 17));
        sizePolicy1.setHeightForWidth(label_24->sizePolicy().hasHeightForWidth());
        label_24->setSizePolicy(sizePolicy1);
        label_24->setFont(font1);
        checkBox_alr_5 = new QCheckBox(groupBox_alr_4);
        checkBox_alr_5->setObjectName(QString::fromUtf8("checkBox_alr_5"));
        checkBox_alr_5->setGeometry(QRect(101, 6, 20, 21));
        sizePolicy1.setHeightForWidth(checkBox_alr_5->sizePolicy().hasHeightForWidth());
        checkBox_alr_5->setSizePolicy(sizePolicy1);
        groupBox_alr_5 = new QGroupBox(centralWidget);
        groupBox_alr_5->setObjectName(QString::fromUtf8("groupBox_alr_5"));
        groupBox_alr_5->setGeometry(QRect(216, 59, 171, 151));
        sizePolicy.setHeightForWidth(groupBox_alr_5->sizePolicy().hasHeightForWidth());
        groupBox_alr_5->setSizePolicy(sizePolicy);
        frame_8 = new QFrame(groupBox_alr_5);
        frame_8->setObjectName(QString::fromUtf8("frame_8"));
        frame_8->setGeometry(QRect(4, 30, 154, 120));
        sizePolicy.setHeightForWidth(frame_8->sizePolicy().hasHeightForWidth());
        frame_8->setSizePolicy(sizePolicy);
        frame_8->setFrameShape(QFrame::StyledPanel);
        frame_8->setFrameShadow(QFrame::Raised);
        frame_8->setLineWidth(1);
        horizontalSlider_alr_6 = new QSlider(frame_8);
        horizontalSlider_alr_6->setObjectName(QString::fromUtf8("horizontalSlider_alr_6"));
        horizontalSlider_alr_6->setGeometry(QRect(9, 41, 131, 29));
        sizePolicy1.setHeightForWidth(horizontalSlider_alr_6->sizePolicy().hasHeightForWidth());
        horizontalSlider_alr_6->setSizePolicy(sizePolicy1);
        horizontalSlider_alr_6->setMaximum(100);
        horizontalSlider_alr_6->setSingleStep(0);
        horizontalSlider_alr_6->setOrientation(Qt::Horizontal);
        horizontalSlider_alr_6->setTickPosition(QSlider::NoTicks);
        line_7 = new QFrame(frame_8);
        line_7->setObjectName(QString::fromUtf8("line_7"));
        line_7->setGeometry(QRect(9, 68, 136, 16));
        sizePolicy1.setHeightForWidth(line_7->sizePolicy().hasHeightForWidth());
        line_7->setSizePolicy(sizePolicy1);
        line_7->setFrameShape(QFrame::HLine);
        line_7->setFrameShadow(QFrame::Sunken);
        label_25 = new QLabel(frame_8);
        label_25->setObjectName(QString::fromUtf8("label_25"));
        label_25->setGeometry(QRect(66, 12, 78, 16));
        sizePolicy1.setHeightForWidth(label_25->sizePolicy().hasHeightForWidth());
        label_25->setSizePolicy(sizePolicy1);
        label_25->setFont(font2);
        label_25->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        doubleSpinBox_alr_6 = new QDoubleSpinBox(frame_8);
        doubleSpinBox_alr_6->setObjectName(QString::fromUtf8("doubleSpinBox_alr_6"));
        doubleSpinBox_alr_6->setGeometry(QRect(10, 8, 50, 27));
        sizePolicy1.setHeightForWidth(doubleSpinBox_alr_6->sizePolicy().hasHeightForWidth());
        doubleSpinBox_alr_6->setSizePolicy(sizePolicy1);
        doubleSpinBox_alr_6->setMaximumSize(QSize(50, 16777215));
        doubleSpinBox_alr_6->setAlignment(Qt::AlignCenter);
        doubleSpinBox_alr_6->setDecimals(1);
        doubleSpinBox_alr_6->setMaximum(5);
        doubleSpinBox_alr_6->setSingleStep(0.1);
        label_26 = new QLabel(frame_8);
        label_26->setObjectName(QString::fromUtf8("label_26"));
        label_26->setGeometry(QRect(72, 90, 72, 16));
        sizePolicy1.setHeightForWidth(label_26->sizePolicy().hasHeightForWidth());
        label_26->setSizePolicy(sizePolicy1);
        label_26->setFont(font2);
        label_26->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_alr_6 = new QLabel(frame_8);
        label_alr_6->setObjectName(QString::fromUtf8("label_alr_6"));
        label_alr_6->setEnabled(true);
        label_alr_6->setGeometry(QRect(10, 86, 35, 25));
        sizePolicy1.setHeightForWidth(label_alr_6->sizePolicy().hasHeightForWidth());
        label_alr_6->setSizePolicy(sizePolicy1);
        label_alr_6->setMinimumSize(QSize(0, 25));
        label_alr_6->setAutoFillBackground(false);
        label_alr_6->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(196, 193, 189);"));
        label_alr_6->setFrameShape(QFrame::StyledPanel);
        label_alr_6->setAlignment(Qt::AlignCenter);
        label_27 = new QLabel(groupBox_alr_5);
        label_27->setObjectName(QString::fromUtf8("label_27"));
        label_27->setGeometry(QRect(8, 6, 87, 17));
        sizePolicy1.setHeightForWidth(label_27->sizePolicy().hasHeightForWidth());
        label_27->setSizePolicy(sizePolicy1);
        label_27->setFont(font1);
        checkBox_alr_6 = new QCheckBox(groupBox_alr_5);
        checkBox_alr_6->setObjectName(QString::fromUtf8("checkBox_alr_6"));
        checkBox_alr_6->setGeometry(QRect(101, 6, 20, 21));
        sizePolicy1.setHeightForWidth(checkBox_alr_6->sizePolicy().hasHeightForWidth());
        checkBox_alr_6->setSizePolicy(sizePolicy1);
        MainWindow->setCentralWidget(centralWidget);
        label->raise();
        pushButton_on->raise();
        lcdNumber->raise();
        label_9->raise();
        groupBox_alr_2->raise();
        groupBox_alr->raise();
        groupBox_alr_3->raise();
        groupBox_alr_4->raise();
        groupBox_alr_5->raise();
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 806, 25));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MainWindow", "Anterior", 0, QApplication::UnicodeUTF8));
        pushButton_on->setText(QApplication::translate("MainWindow", "On", 0, QApplication::UnicodeUTF8));
        label_9->setText(QApplication::translate("MainWindow", "Run Time", 0, QApplication::UnicodeUTF8));
        groupBox_alr_2->setTitle(QString());
        label_16->setText(QApplication::translate("MainWindow", "setpoint (psi)", 0, QApplication::UnicodeUTF8));
        label_17->setText(QApplication::translate("MainWindow", "current (psi)", 0, QApplication::UnicodeUTF8));
        label_alr_3->setText(QApplication::translate("MainWindow", "0.0", 0, QApplication::UnicodeUTF8));
        label_18->setText(QApplication::translate("MainWindow", "Lower Right", 0, QApplication::UnicodeUTF8));
        checkBox_alr_3->setText(QString());
        groupBox_alr->setTitle(QString());
        label_11->setText(QApplication::translate("MainWindow", "setpoint (psi)", 0, QApplication::UnicodeUTF8));
        label_alr->setText(QApplication::translate("MainWindow", "0.0", 0, QApplication::UnicodeUTF8));
        label_13->setText(QApplication::translate("MainWindow", "current (psi)", 0, QApplication::UnicodeUTF8));
        label_10->setText(QApplication::translate("MainWindow", "Lower Right", 0, QApplication::UnicodeUTF8));
        checkBox_alr->setText(QString());
        groupBox_alr_3->setTitle(QString());
        label_19->setText(QApplication::translate("MainWindow", "setpoint (psi)", 0, QApplication::UnicodeUTF8));
        label_20->setText(QApplication::translate("MainWindow", "current (psi)", 0, QApplication::UnicodeUTF8));
        label_alr_4->setText(QApplication::translate("MainWindow", "0.0", 0, QApplication::UnicodeUTF8));
        label_21->setText(QApplication::translate("MainWindow", "Upper Right", 0, QApplication::UnicodeUTF8));
        checkBox_alr_4->setText(QString());
        groupBox_alr_4->setTitle(QString());
        label_22->setText(QApplication::translate("MainWindow", "setpoint (psi)", 0, QApplication::UnicodeUTF8));
        label_23->setText(QApplication::translate("MainWindow", "current (psi)", 0, QApplication::UnicodeUTF8));
        label_alr_5->setText(QApplication::translate("MainWindow", "0.0", 0, QApplication::UnicodeUTF8));
        label_24->setText(QApplication::translate("MainWindow", "Lower Left", 0, QApplication::UnicodeUTF8));
        checkBox_alr_5->setText(QString());
        groupBox_alr_5->setTitle(QString());
        label_25->setText(QApplication::translate("MainWindow", "setpoint (psi)", 0, QApplication::UnicodeUTF8));
        label_26->setText(QApplication::translate("MainWindow", "current (psi)", 0, QApplication::UnicodeUTF8));
        label_alr_6->setText(QApplication::translate("MainWindow", "0.0", 0, QApplication::UnicodeUTF8));
        label_27->setText(QApplication::translate("MainWindow", "Upper Left", 0, QApplication::UnicodeUTF8));
        checkBox_alr_6->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
