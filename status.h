#ifndef STATUS_H
#define STATUS_H

#include <QDialog>

namespace Ui {
class status;
}

class status : public QDialog
{
    Q_OBJECT

public:
    explicit status(QWidget *parent = 0);
    ~status();

private:
    Ui::status *ui;
};

#endif // STATUS_H
