import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class ECPasswordGUI extends Application {

    private TextField memorableField;
    private TextField lengthField;
    private TextArea outputBox;
    private Label statusLabel;

    @Override
    public void start(Stage stage) {
        stage.setTitle("EC-Based Strong Password Generator");

        Label title = new Label("Strong Password Generator");
        title.setStyle("-fx-font-size: 20px; -fx-text-fill: #4CAF50;");

        Label lblMem = new Label("Memorable Password:");
        memorableField = new TextField();
        Label lblLen = new Label("Desired Length:");
        lengthField = new TextField();

        Button btnGen = new Button("Generate Password");
        btnGen.setStyle("-fx-background-color: #4CAF50; -fx-text-fill: white;");
        btnGen.setOnAction(e -> generatePassword());

        outputBox = new TextArea();
        outputBox.setEditable(false);
        outputBox.setPrefRowCount(2);
        outputBox.setStyle("-fx-control-inner-background: #1E1E1E; -fx-text-fill: #00FF7F;");

        Button btnSave = new Button("Save to File");
        btnSave.setStyle("-fx-background-color: #2196F3; -fx-text-fill: white;");
        btnSave.setOnAction(e -> saveToFile());

        statusLabel = new Label("Ready");
        statusLabel.setStyle("-fx-text-fill: gray;");

        VBox root = new VBox(10, title,
                lblMem, memorableField,
                lblLen, lengthField,
                btnGen, outputBox, btnSave, statusLabel);
        root.setPadding(new Insets(20));
        root.setStyle("-fx-background-color: #141414;");

        stage.setScene(new Scene(root, 500, 400));
        stage.show();
    }

    private void generatePassword() {
        String memorable = memorableField.getText().trim();
        String lenText = lengthField.getText().trim();

        if (memorable.isEmpty() || lenText.isEmpty()) {
            statusLabel.setText("Please fill in all fields.");
            return;
        }

        try {
            int length = Integer.parseInt(lenText);
            String password = ECPasswordGenerator.generateECPassword(memorable, length);
            outputBox.setText(password);
            statusLabel.setText("Password generated successfully.");
        } catch (Exception ex) {
            statusLabel.setText("Error: " + ex.getMessage());
            ex.printStackTrace();
        }
    }

    private void saveToFile() {
        String text = outputBox.getText();
        if (text.isEmpty()) {
            statusLabel.setText("Nothing to save.");
            return;
        }
        try {
            java.nio.file.Files.writeString(java.nio.file.Path.of("ec_strong_password.txt"), text);
            statusLabel.setText("Saved to ec_strong_password.txt");
        } catch (Exception e) {
            statusLabel.setText("Save failed: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        launch();
    }
}
