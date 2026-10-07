// Small Java server using Spark (https://sparkjava.com/) to serve modules.json
// Run with: add spark-core dependency and run this main
import static spark.Spark.*;
import java.nio.file.*;

public class Server {
    public static void main(String[] args) {
        port(4567);
        get("/api/modules", (req, res) -> {
            res.type("application/json");
            try {
                return new String(Files.readAllBytes(Paths.get("modules.json")));
            } catch (Exception e) {
                res.status(500);
                return "{\"error\":\"file not found\"}";
            }
        });

        get("/", (req, res) -> {
            res.type("text/html");
            try {
                return new String(Files.readAllBytes(Paths.get("trade-with-suli.html")));
            } catch (Exception e) {
                res.status(500);
                return "trade-with-suli.html not found";
            }
        });
    }
}
