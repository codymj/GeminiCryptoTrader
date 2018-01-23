/********************************************************************************
** Form generated from reading UI file 'MainWindow.ui'
**
** Created by: Qt User Interface Compiler version 5.10.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *action_Edit;
    QAction *setupAction;
    QAction *buyAction;
    QAction *sellAction;
    QAction *conditionalAction;
    QAction *genDepositAction;
    QAction *withdrawToAction;
    QAction *exitAction;
    QAction *optionsAction;
    QAction *notificationsAction;
    QAction *hideStatusbarAction;
    QAction *showOrderbookAction;
    QAction *action_About;
    QAction *action_Visit_Gemini_API_Docs;
    QAction *action_Gemini_Exchange;
    QWidget *centralwidget;
    QGridLayout *gridLayout_7;
    QVBoxLayout *verticalLayout;
    QGroupBox *balanceGroupBox;
    QGridLayout *gridLayout;
    QLabel *label;
    QLabel *accountBalanceLabel;
    QLabel *label_3;
    QLabel *btcBalanceLabel;
    QLabel *ethBalanceLabel;
    QLabel *label_2;
    QGroupBox *availableGroupBox;
    QGridLayout *gridLayout_2;
    QLabel *usdAvailableLabel;
    QLabel *label_5;
    QLabel *btcAvailableLabel;
    QLabel *label_4;
    QLabel *label_6;
    QLabel *ethAvailableLabel;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer;
    QPushButton *disconnectButton;
    QPushButton *connectButton;
    QTabWidget *currencyTabWidget;
    QWidget *btcTab;
    QGridLayout *gridLayout_4;
    QGridLayout *gridLayout_3;
    QLabel *label_7;
    QLabel *btcLastPriceLabel;
    QLabel *label_8;
    QLabel *btcDeltaLabel;
    QLabel *label_9;
    QLabel *btcRangeLabel;
    QSpacerItem *horizontalSpacer_3;
    QGraphicsView *btcGraphView;
    QWidget *ethTab;
    QGridLayout *gridLayout_6;
    QGridLayout *gridLayout_5;
    QLabel *ethLastPriceLabel;
    QLabel *label_11;
    QLabel *label_10;
    QLabel *ethDeltaLabel;
    QLabel *label_12;
    QLabel *ethRangeLabel;
    QSpacerItem *horizontalSpacer_2;
    QGraphicsView *ethGraphView;
    QMenuBar *menuBar;
    QMenu *menuFile;
    QMenu *menuEdit;
    QMenu *menuView;
    QMenu *menuHelp;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(640, 360);
        MainWindow->setMinimumSize(QSize(640, 360));
        MainWindow->setMaximumSize(QSize(640, 360));
        action_Edit = new QAction(MainWindow);
        action_Edit->setObjectName(QStringLiteral("action_Edit"));
        setupAction = new QAction(MainWindow);
        setupAction->setObjectName(QStringLiteral("setupAction"));
        buyAction = new QAction(MainWindow);
        buyAction->setObjectName(QStringLiteral("buyAction"));
        sellAction = new QAction(MainWindow);
        sellAction->setObjectName(QStringLiteral("sellAction"));
        conditionalAction = new QAction(MainWindow);
        conditionalAction->setObjectName(QStringLiteral("conditionalAction"));
        genDepositAction = new QAction(MainWindow);
        genDepositAction->setObjectName(QStringLiteral("genDepositAction"));
        withdrawToAction = new QAction(MainWindow);
        withdrawToAction->setObjectName(QStringLiteral("withdrawToAction"));
        exitAction = new QAction(MainWindow);
        exitAction->setObjectName(QStringLiteral("exitAction"));
        optionsAction = new QAction(MainWindow);
        optionsAction->setObjectName(QStringLiteral("optionsAction"));
        notificationsAction = new QAction(MainWindow);
        notificationsAction->setObjectName(QStringLiteral("notificationsAction"));
        hideStatusbarAction = new QAction(MainWindow);
        hideStatusbarAction->setObjectName(QStringLiteral("hideStatusbarAction"));
        showOrderbookAction = new QAction(MainWindow);
        showOrderbookAction->setObjectName(QStringLiteral("showOrderbookAction"));
        action_About = new QAction(MainWindow);
        action_About->setObjectName(QStringLiteral("action_About"));
        action_Visit_Gemini_API_Docs = new QAction(MainWindow);
        action_Visit_Gemini_API_Docs->setObjectName(QStringLiteral("action_Visit_Gemini_API_Docs"));
        action_Gemini_Exchange = new QAction(MainWindow);
        action_Gemini_Exchange->setObjectName(QStringLiteral("action_Gemini_Exchange"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        gridLayout_7 = new QGridLayout(centralwidget);
        gridLayout_7->setObjectName(QStringLiteral("gridLayout_7"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        balanceGroupBox = new QGroupBox(centralwidget);
        balanceGroupBox->setObjectName(QStringLiteral("balanceGroupBox"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::MinimumExpanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(balanceGroupBox->sizePolicy().hasHeightForWidth());
        balanceGroupBox->setSizePolicy(sizePolicy);
        gridLayout = new QGridLayout(balanceGroupBox);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        label = new QLabel(balanceGroupBox);
        label->setObjectName(QStringLiteral("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);

        accountBalanceLabel = new QLabel(balanceGroupBox);
        accountBalanceLabel->setObjectName(QStringLiteral("accountBalanceLabel"));

        gridLayout->addWidget(accountBalanceLabel, 0, 1, 1, 1);

        label_3 = new QLabel(balanceGroupBox);
        label_3->setObjectName(QStringLiteral("label_3"));

        gridLayout->addWidget(label_3, 2, 0, 1, 1);

        btcBalanceLabel = new QLabel(balanceGroupBox);
        btcBalanceLabel->setObjectName(QStringLiteral("btcBalanceLabel"));

        gridLayout->addWidget(btcBalanceLabel, 1, 1, 1, 1);

        ethBalanceLabel = new QLabel(balanceGroupBox);
        ethBalanceLabel->setObjectName(QStringLiteral("ethBalanceLabel"));

        gridLayout->addWidget(ethBalanceLabel, 2, 1, 1, 1);

        label_2 = new QLabel(balanceGroupBox);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout->addWidget(label_2, 1, 0, 1, 1);


        verticalLayout->addWidget(balanceGroupBox);

        availableGroupBox = new QGroupBox(centralwidget);
        availableGroupBox->setObjectName(QStringLiteral("availableGroupBox"));
        sizePolicy.setHeightForWidth(availableGroupBox->sizePolicy().hasHeightForWidth());
        availableGroupBox->setSizePolicy(sizePolicy);
        gridLayout_2 = new QGridLayout(availableGroupBox);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        usdAvailableLabel = new QLabel(availableGroupBox);
        usdAvailableLabel->setObjectName(QStringLiteral("usdAvailableLabel"));

        gridLayout_2->addWidget(usdAvailableLabel, 0, 1, 1, 1);

        label_5 = new QLabel(availableGroupBox);
        label_5->setObjectName(QStringLiteral("label_5"));

        gridLayout_2->addWidget(label_5, 1, 0, 1, 1);

        btcAvailableLabel = new QLabel(availableGroupBox);
        btcAvailableLabel->setObjectName(QStringLiteral("btcAvailableLabel"));

        gridLayout_2->addWidget(btcAvailableLabel, 1, 1, 1, 1);

        label_4 = new QLabel(availableGroupBox);
        label_4->setObjectName(QStringLiteral("label_4"));

        gridLayout_2->addWidget(label_4, 0, 0, 1, 1);

        label_6 = new QLabel(availableGroupBox);
        label_6->setObjectName(QStringLiteral("label_6"));

        gridLayout_2->addWidget(label_6, 2, 0, 1, 1);

        ethAvailableLabel = new QLabel(availableGroupBox);
        ethAvailableLabel->setObjectName(QStringLiteral("ethAvailableLabel"));

        gridLayout_2->addWidget(ethAvailableLabel, 2, 1, 1, 1);


        verticalLayout->addWidget(availableGroupBox);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Preferred, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        disconnectButton = new QPushButton(centralwidget);
        disconnectButton->setObjectName(QStringLiteral("disconnectButton"));

        horizontalLayout->addWidget(disconnectButton);

        connectButton = new QPushButton(centralwidget);
        connectButton->setObjectName(QStringLiteral("connectButton"));

        horizontalLayout->addWidget(connectButton);


        verticalLayout->addLayout(horizontalLayout);


        gridLayout_7->addLayout(verticalLayout, 0, 1, 1, 1);

        currencyTabWidget = new QTabWidget(centralwidget);
        currencyTabWidget->setObjectName(QStringLiteral("currencyTabWidget"));
        QSizePolicy sizePolicy1(QSizePolicy::MinimumExpanding, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(currencyTabWidget->sizePolicy().hasHeightForWidth());
        currencyTabWidget->setSizePolicy(sizePolicy1);
        btcTab = new QWidget();
        btcTab->setObjectName(QStringLiteral("btcTab"));
        gridLayout_4 = new QGridLayout(btcTab);
        gridLayout_4->setObjectName(QStringLiteral("gridLayout_4"));
        gridLayout_3 = new QGridLayout();
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        label_7 = new QLabel(btcTab);
        label_7->setObjectName(QStringLiteral("label_7"));

        gridLayout_3->addWidget(label_7, 0, 0, 1, 1);

        btcLastPriceLabel = new QLabel(btcTab);
        btcLastPriceLabel->setObjectName(QStringLiteral("btcLastPriceLabel"));

        gridLayout_3->addWidget(btcLastPriceLabel, 0, 1, 1, 1);

        label_8 = new QLabel(btcTab);
        label_8->setObjectName(QStringLiteral("label_8"));

        gridLayout_3->addWidget(label_8, 1, 0, 1, 1);

        btcDeltaLabel = new QLabel(btcTab);
        btcDeltaLabel->setObjectName(QStringLiteral("btcDeltaLabel"));

        gridLayout_3->addWidget(btcDeltaLabel, 1, 1, 1, 1);

        label_9 = new QLabel(btcTab);
        label_9->setObjectName(QStringLiteral("label_9"));

        gridLayout_3->addWidget(label_9, 2, 0, 1, 1);

        btcRangeLabel = new QLabel(btcTab);
        btcRangeLabel->setObjectName(QStringLiteral("btcRangeLabel"));

        gridLayout_3->addWidget(btcRangeLabel, 2, 1, 1, 1);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_3->addItem(horizontalSpacer_3, 1, 2, 1, 1);


        gridLayout_4->addLayout(gridLayout_3, 0, 0, 1, 1);

        btcGraphView = new QGraphicsView(btcTab);
        btcGraphView->setObjectName(QStringLiteral("btcGraphView"));

        gridLayout_4->addWidget(btcGraphView, 1, 0, 1, 1);

        currencyTabWidget->addTab(btcTab, QString());
        ethTab = new QWidget();
        ethTab->setObjectName(QStringLiteral("ethTab"));
        gridLayout_6 = new QGridLayout(ethTab);
        gridLayout_6->setObjectName(QStringLiteral("gridLayout_6"));
        gridLayout_5 = new QGridLayout();
        gridLayout_5->setObjectName(QStringLiteral("gridLayout_5"));
        ethLastPriceLabel = new QLabel(ethTab);
        ethLastPriceLabel->setObjectName(QStringLiteral("ethLastPriceLabel"));

        gridLayout_5->addWidget(ethLastPriceLabel, 0, 1, 1, 1);

        label_11 = new QLabel(ethTab);
        label_11->setObjectName(QStringLiteral("label_11"));

        gridLayout_5->addWidget(label_11, 0, 0, 1, 1);

        label_10 = new QLabel(ethTab);
        label_10->setObjectName(QStringLiteral("label_10"));

        gridLayout_5->addWidget(label_10, 1, 0, 1, 1);

        ethDeltaLabel = new QLabel(ethTab);
        ethDeltaLabel->setObjectName(QStringLiteral("ethDeltaLabel"));

        gridLayout_5->addWidget(ethDeltaLabel, 1, 1, 1, 1);

        label_12 = new QLabel(ethTab);
        label_12->setObjectName(QStringLiteral("label_12"));

        gridLayout_5->addWidget(label_12, 2, 0, 1, 1);

        ethRangeLabel = new QLabel(ethTab);
        ethRangeLabel->setObjectName(QStringLiteral("ethRangeLabel"));

        gridLayout_5->addWidget(ethRangeLabel, 2, 1, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_5->addItem(horizontalSpacer_2, 1, 2, 1, 1);


        gridLayout_6->addLayout(gridLayout_5, 0, 0, 1, 1);

        ethGraphView = new QGraphicsView(ethTab);
        ethGraphView->setObjectName(QStringLiteral("ethGraphView"));

        gridLayout_6->addWidget(ethGraphView, 1, 0, 1, 1);

        currencyTabWidget->addTab(ethTab, QString());

        gridLayout_7->addWidget(currencyTabWidget, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 640, 22));
        menuFile = new QMenu(menuBar);
        menuFile->setObjectName(QStringLiteral("menuFile"));
        menuEdit = new QMenu(menuBar);
        menuEdit->setObjectName(QStringLiteral("menuEdit"));
        menuView = new QMenu(menuBar);
        menuView->setObjectName(QStringLiteral("menuView"));
        menuHelp = new QMenu(menuBar);
        menuHelp->setObjectName(QStringLiteral("menuHelp"));
        MainWindow->setMenuBar(menuBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuFile->menuAction());
        menuBar->addAction(menuEdit->menuAction());
        menuBar->addAction(menuView->menuAction());
        menuBar->addAction(menuHelp->menuAction());
        menuFile->addAction(setupAction);
        menuFile->addSeparator();
        menuFile->addAction(buyAction);
        menuFile->addAction(sellAction);
        menuFile->addAction(conditionalAction);
        menuFile->addSeparator();
        menuFile->addAction(genDepositAction);
        menuFile->addAction(withdrawToAction);
        menuFile->addSeparator();
        menuFile->addAction(exitAction);
        menuEdit->addAction(optionsAction);
        menuEdit->addSeparator();
        menuEdit->addAction(notificationsAction);
        menuView->addAction(hideStatusbarAction);
        menuView->addAction(showOrderbookAction);
        menuHelp->addAction(action_About);
        menuHelp->addAction(action_Visit_Gemini_API_Docs);
        menuHelp->addAction(action_Gemini_Exchange);

        retranslateUi(MainWindow);

        currencyTabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Gemini Crypto Trader", nullptr));
        action_Edit->setText(QApplication::translate("MainWindow", "&Edit", nullptr));
        setupAction->setText(QApplication::translate("MainWindow", "Se&tup", nullptr));
        buyAction->setText(QApplication::translate("MainWindow", "&Buy", nullptr));
        sellAction->setText(QApplication::translate("MainWindow", "&Sell", nullptr));
        conditionalAction->setText(QApplication::translate("MainWindow", "&Conditional", nullptr));
        genDepositAction->setText(QApplication::translate("MainWindow", "&Generate Deposit Address", nullptr));
        withdrawToAction->setText(QApplication::translate("MainWindow", "&Withdraw To...", nullptr));
        exitAction->setText(QApplication::translate("MainWindow", "&Exit", nullptr));
        optionsAction->setText(QApplication::translate("MainWindow", "&Options", nullptr));
        notificationsAction->setText(QApplication::translate("MainWindow", "&Notifications", nullptr));
        hideStatusbarAction->setText(QApplication::translate("MainWindow", "&Hide Statusbar", nullptr));
        showOrderbookAction->setText(QApplication::translate("MainWindow", "&Show Orderbook", nullptr));
        action_About->setText(QApplication::translate("MainWindow", "&About", nullptr));
        action_Visit_Gemini_API_Docs->setText(QApplication::translate("MainWindow", "&Visit Gemini API Docs", nullptr));
        action_Gemini_Exchange->setText(QApplication::translate("MainWindow", "Visit &Gemini Exchange", nullptr));
        balanceGroupBox->setTitle(QApplication::translate("MainWindow", "Balances:", nullptr));
        label->setText(QApplication::translate("MainWindow", "Account Balance:", nullptr));
        accountBalanceLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        label_3->setText(QApplication::translate("MainWindow", "ETH Balance:", nullptr));
        btcBalanceLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        ethBalanceLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "BTC Balance:", nullptr));
        availableGroupBox->setTitle(QApplication::translate("MainWindow", "Available for Trading:", nullptr));
        usdAvailableLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        label_5->setText(QApplication::translate("MainWindow", "BTC Available:", nullptr));
        btcAvailableLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        label_4->setText(QApplication::translate("MainWindow", "USD Available:", nullptr));
        label_6->setText(QApplication::translate("MainWindow", "ETH Available:", nullptr));
        ethAvailableLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        disconnectButton->setText(QApplication::translate("MainWindow", "&Disconnect", nullptr));
        connectButton->setText(QApplication::translate("MainWindow", "&Connect", nullptr));
        label_7->setText(QApplication::translate("MainWindow", "Last Price:", nullptr));
        btcLastPriceLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        label_8->setText(QApplication::translate("MainWindow", "24-Hour \316\224:", nullptr));
        btcDeltaLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        label_9->setText(QApplication::translate("MainWindow", "24-Hour Range:", nullptr));
        btcRangeLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        currencyTabWidget->setTabText(currencyTabWidget->indexOf(btcTab), QApplication::translate("MainWindow", "BTC", nullptr));
        ethLastPriceLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        label_11->setText(QApplication::translate("MainWindow", "Last Price:", nullptr));
        label_10->setText(QApplication::translate("MainWindow", "24-Hour \316\224:", nullptr));
        ethDeltaLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        label_12->setText(QApplication::translate("MainWindow", "24-Hour Range:", nullptr));
        ethRangeLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        currencyTabWidget->setTabText(currencyTabWidget->indexOf(ethTab), QApplication::translate("MainWindow", "ETH", nullptr));
        menuFile->setTitle(QApplication::translate("MainWindow", "&File", nullptr));
        menuEdit->setTitle(QApplication::translate("MainWindow", "&Edit", nullptr));
        menuView->setTitle(QApplication::translate("MainWindow", "&View", nullptr));
        menuHelp->setTitle(QApplication::translate("MainWindow", "&Help", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
