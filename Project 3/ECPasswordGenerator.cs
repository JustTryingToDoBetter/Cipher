using System;
using System.IO;
using System.Linq;
using System.Windows.Forms;
using System.Collections.Generic;
using System.Globalization;

namespace ECPasswordGenerator
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        // === Evolutionary-Computed Cipher (from Project 1) ===
        private double EcFormula(double row)
        {
            // Equivalent to the Python nonlinear function
            return 0.432357 + (-0.498752 * Math.Cos(
                0.594808 * (-4.10993 * Math.Cosh(row) -
                (0.590558 + Math.Atanh(Math.Cos(
                Math.Tan(Math.Cos(row / (-0.00153462))) + row * row))))));
        }

        // === Iterative Stream Generator ===
        private List<double> GenerateRandomNumberStream(double seed, int length)
        {
            var stream = new List<double> { seed };
            for (int i = 1; i < length; i++)
            {
                stream.Add(EcFormula(stream[i - 1]));
            }
            return stream;
        }

        // === Uniform Transform (rank-based normalisation) ===
        private List<double> TransformToUniform(List<double> inputArray)
        {
            var sorted = inputArray
                .Select((v, i) => new { Value = v, Index = i })
                .OrderBy(x => x.Value)
                .Select((x, rank) => new { x.Index, Rank = rank })
                .ToDictionary(x => x.Index, x => x.Rank);

            int n = inputArray.Count;
            var uniform = new List<double>(n);
            for (int i = 0; i < n; i++)
            {
                uniform.Add((double)sorted[i] / (n - 1));
            }
            return uniform;
        }

        // === Strong-Password Generation ===
        private string GenerateEcStrongPassword(string memorablePassword, int length)
        {
            if (length < memorablePassword.Length)
                throw new Exception("Length must be >= length of memorable password.");

            double seed = memorablePassword.Sum(c => (double)c / 256.0);
            var rawStream = GenerateRandomNumberStream(seed, length);
            var uniform = TransformToUniform(rawStream);

            var chars = uniform.Select(v =>
                (char)(Math.Abs(v * 1000 % 94) + 33)).ToArray();

            return new string(chars);
        }

        // === GUI Event Handlers ===
        private void BtnGenerate_Click(object sender, EventArgs e)
        {
            try
            {
                string weak = txtWeakPassword.Text;
                if (string.IsNullOrWhiteSpace(weak))
                    throw new Exception("Please enter a memorable password.");

                int length = (int)numLength.Value;
                string strong = GenerateEcStrongPassword(weak, length);

                txtOutput.Text = strong;
                File.WriteAllText("ec_strong_password.txt",
                    $"Memorable password: {weak}\nStrong password: {strong}\n");
                MessageBox.Show("Strong password saved to ec_strong_password.txt", 
                    "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message,
                    "Generation Failed", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
