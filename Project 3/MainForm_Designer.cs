namespace ECPasswordGenerator
{
    partial class MainForm
    {
        private System.ComponentModel.IContainer components = null;
        private TextBox txtWeakPassword;
        private NumericUpDown numLength;
        private TextBox txtOutput;
        private Button btnGenerate;
        private Label lblWeak;
        private Label lblLength;
        private Label lblOutput;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null)) components.Dispose();
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            this.txtWeakPassword = new TextBox();
            this.numLength = new NumericUpDown();
            this.txtOutput = new TextBox();
            this.btnGenerate = new Button();
            this.lblWeak = new Label();
            this.lblLength = new Label();
            this.lblOutput = new Label();
            ((System.ComponentModel.ISupportInitialize)(this.numLength)).BeginInit();
            this.SuspendLayout();
            // 
            // lblWeak
            // 
            this.lblWeak.Text = "Memorable password:";
            this.lblWeak.Location = new System.Drawing.Point(12, 20);
            this.lblWeak.AutoSize = true;
            // 
            // txtWeakPassword
            // 
            this.txtWeakPassword.Location = new System.Drawing.Point(180, 18);
            this.txtWeakPassword.Width = 220;
            // 
            // lblLength
            // 
            this.lblLength.Text = "Desired length:";
            this.lblLength.Location = new System.Drawing.Point(12, 55);
            this.lblLength.AutoSize = true;
            // 
            // numLength
            // 
            this.numLength.Location = new System.Drawing.Point(180, 53);
            this.numLength.Minimum = 8;
            this.numLength.Maximum = 128;
            this.numLength.Value = 16;
            // 
            // lblOutput
            // 
            this.lblOutput.Text = "Generated strong password:";
            this.lblOutput.Location = new System.Drawing.Point(12, 95);
            this.lblOutput.AutoSize = true;
            // 
            // txtOutput
            // 
            this.txtOutput.Location = new System.Drawing.Point(15, 115);
            this.txtOutput.Width = 385;
            this.txtOutput.Height = 60;
            this.txtOutput.Multiline = true;
            this.txtOutput.ReadOnly = true;
            // 
            // btnGenerate
            // 
            this.btnGenerate.Text = "Generate Password";
            this.btnGenerate.Location = new System.Drawing.Point(15, 190);
            this.btnGenerate.Click += new EventHandler(this.BtnGenerate_Click);
            // 
            // MainForm
            // 
            this.ClientSize = new System.Drawing.Size(420, 240);
            this.Controls.Add(this.lblWeak);
            this.Controls.Add(this.txtWeakPassword);
            this.Controls.Add(this.lblLength);
            this.Controls.Add(this.numLength);
            this.Controls.Add(this.lblOutput);
            this.Controls.Add(this.txtOutput);
            this.Controls.Add(this.btnGenerate);
            this.Text = "EC-Based Strong Password Generator";
            ((System.ComponentModel.ISupportInitialize)(this.numLength)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();
        }
    }
}
