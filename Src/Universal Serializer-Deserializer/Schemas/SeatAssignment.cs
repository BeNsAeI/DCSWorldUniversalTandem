namespace DCSWorldUniversalTandem.SerialDeserial
{
    using System;
    using System.Collections.Generic;

    using System.Globalization;
    using Newtonsoft.Json;
    using Newtonsoft.Json.Converters;

    public partial class SeatAssignment
    {
        [JsonProperty("seatName")]
        public string SeatName { get; set; }

        [JsonProperty("seatId")]
        [JsonConverter(typeof(ParseStringConverter))]
        public long SeatId { get; set; }

        [JsonProperty("userName", NullValueHandling = NullValueHandling.Ignore)]
        public string UserName { get; set; }
    }
}