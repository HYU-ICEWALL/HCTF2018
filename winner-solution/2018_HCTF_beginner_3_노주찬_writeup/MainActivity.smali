.class public Licewall/decompileme/MainActivity;
.super Landroid/support/v7/app/AppCompatActivity;
.source "MainActivity.java"


# instance fields
.field real_flag:Ljava/lang/String;


# direct methods
.method public constructor <init>()V
    .locals 1

    .line 6
    invoke-direct {p0}, Landroid/support/v7/app/AppCompatActivity;-><init>()V

    .line 8
    const-string v0, "FLAG{Trust_th1s_5tr1ng}"

    iput-object v0, p0, Licewall/decompileme/MainActivity;->real_flag:Ljava/lang/String;

    return-void
.end method


# virtual methods
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 1
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .line 11
    invoke-super {p0, p1}, Landroid/support/v7/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    .line 12
    const v0, 0x7f09001c

    invoke-virtual {p0, v0}, Licewall/decompileme/MainActivity;->setContentView(I)V

    .line 13
    return-void
.end method

