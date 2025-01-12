import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class DigitalClock {
    public static void main(String[] args) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss");

        while (true) {
            // Get the current time
            LocalTime currentTime = LocalTime.now();
            
            // Format the time as HH:mm:ss
            String timeString = currentTime.format(formatter);
            
            // Display the time
            System.out.print("\rCurrent Time: " + timeString);
            
            try {
                // Wait for 1 second
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.out.println("Clock interrupted");
            }
        }
    }
}
